"""
Collects public GitHub activity for the start page's "Patch notes" panel.

  python tools/github_activity.py

Writes assets/data/activity.json:
  calendar  last 26 weeks of contributions (one entry per day)
  stats     contributions in the last year, current streak, active days
  notes     latest commit messages from your public repositories
A GitHub Action (.github/workflows/activity.yml) runs this every day, so the
panel stays fresh without anyone touching it. Standard library only.

With GITHUB_TOKEN set (the Action sets it) the calendar comes from GitHub's own
GraphQL API; without it, from the public github-contributions-api.jogruber.de mirror.
"""
import datetime as dt
import json
import os
import pathlib
import urllib.request

USER = 'AlexPaisDev'
OUT = pathlib.Path(__file__).resolve().parent.parent / 'assets' / 'data' / 'activity.json'
TOKEN = os.environ.get('GITHUB_TOKEN')
WEEKS = 26          # columns in the calendar
NOTES = 6           # commit messages shown
SKIP_REPOS = {USER}  # profile README repo: only bot "summary card" commits


def get(url, body=None):
    headers = {'User-Agent': 'alexpaisdev-site', 'Accept': 'application/json'}
    if TOKEN and 'api.github.com' in url:
        headers['Authorization'] = f'Bearer {TOKEN}'
    data = json.dumps(body).encode() if body else None
    with urllib.request.urlopen(urllib.request.Request(url, data, headers), timeout=30) as r:
        return json.load(r)


def contribution_days():
    """{'YYYY-MM-DD': count} for about the last year."""
    if TOKEN:
        q = ('query($u:String!){user(login:$u){contributionsCollection{contributionCalendar{'
             'weeks{contributionDays{date contributionCount}}}}}}')
        res = get('https://api.github.com/graphql', {'query': q, 'variables': {'u': USER}})
        weeks = res['data']['user']['contributionsCollection']['contributionCalendar']['weeks']
        return {d['date']: d['contributionCount'] for w in weeks for d in w['contributionDays']}
    res = get(f'https://github-contributions-api.jogruber.de/v4/{USER}?y=last')
    return {d['date']: d['count'] for d in res['contributions']}


def latest_commits():
    repos = [r for r in get(f'https://api.github.com/users/{USER}/repos?sort=pushed&per_page=8')
             if not r['fork'] and r['name'] not in SKIP_REPOS]
    notes = []
    for repo in repos[:6]:
        # at most 2 per repo, so one busy project doesn't fill the whole list
        for c in get(f"https://api.github.com/repos/{USER}/{repo['name']}/commits?author={USER}&per_page=2"):
            msg = c['commit']['message'].split('\n')[0].strip()
            notes.append({'repo': repo['name'], 'date': c['commit']['author']['date'][:10],
                          'message': msg[:90] + ('…' if len(msg) > 90 else ''), 'url': c['html_url']})
    notes.sort(key=lambda n: n['date'], reverse=True)
    return notes[:NOTES]


def main():
    days = contribution_days()
    today = dt.date.today()
    # calendar starts on a Sunday so each column is one week, like GitHub's
    start = today - dt.timedelta(days=(today.weekday() + 1) % 7 + 7 * (WEEKS - 1))
    calendar = [{'date': str(start + dt.timedelta(i)), 'count': days.get(str(start + dt.timedelta(i)), 0)}
                for i in range((today - start).days + 1)]
    year = [days.get(str(today - dt.timedelta(i)), 0) for i in range(365)]
    streak, i = 0, 0 if year[0] else 1          # a streak still counts if today has nothing yet
    while i < len(year) and year[i]:
        streak, i = streak + 1, i + 1
    data = {
        'user': USER,
        'updated': today.isoformat(),
        'stats': {'year': sum(year), 'streak': streak, 'activeDays': sum(1 for n in year if n), 'best': max(year)},
        'calendar': calendar,
        'notes': latest_commits(),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    print(f"wrote {OUT.name}: {data['stats']}, {len(data['notes'])} notes")


if __name__ == '__main__':
    main()
