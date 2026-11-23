# alexpaisdev.github.io

Personal site of **Alexandre Pais**, live at <https://alexpaisdev.github.io/>.

One person, two sides. Visitors pick one on the start page:

| Side | Address | Look | CV (English / Portuguese) |
|---|---|---|---|
| **Data & AI** | [`/data/`](https://alexpaisdev.github.io/data/) | blue, sea, waves | `Alexandre_Pais_CV_Data_EN.pdf` / `Alexandre_Pais_CV_Data_PT.pdf` |
| **Software engineering** | [`/software/`](https://alexpaisdev.github.io/software/) | red, land, mountains | `Alexandre_Pais_CV_EN.pdf` / `Alexandre_Pais_CV_PT.pdf` |

Send the matching address with each application. Each side's "Save CV" button gives the CV in the language the visitor picked. Old links ending in `?track=data` or `?track=software` still redirect to the right side. (The software CVs keep their original filenames so links shared before still work.)

Both sides use the same pixel interface, in the spirit of GBA-era handheld RPGs: windows, dialog boxes, a ▶ cursor and a quest log. Every page works in English and Portuguese.

Plain HTML, CSS and JavaScript. No build step, no framework, no dependencies.

## Files

```text
index.html              start page: pick a side (left blue, right red)
data/index.html         Data & AI side
software/index.html     Software side (same structure and classes as the data side)
download.html           every CV in one list
404.html                "page not found"
Alexandre_Pais_CV_*.pdf the four CVs (built by tools/cv, filenames are linked from the pages)

assets/css/pixel.css    the whole pixel interface + the two colour themes
assets/css/home.css     layout of the start page only
assets/js/site.js       behaviour for every page (language, menus, typewriter, icons, form…)
assets/js/i18n/         Portuguese text
  pt-common.js            shared by both sides
  pt-data.js              data side only
  pt-software.js          software side only
  pt-home.js              start page
assets/img/             favicon, home-screen icon, link-preview image (og-image.png)
assets/data/activity.json  GitHub activity for the start page's Patch notes (refreshed daily)

tools/check_site.py     run after editing: missing translations, broken links, duplicate ids
tools/pixel_art.py      regenerates the pixel art (window frames, tiles, scenery, icons, preview image)
tools/github_activity.py  collects the GitHub activity into assets/data/activity.json
.github/workflows/activity.yml  runs that script every day and commits the result
tools/cv/content.py     the text of all four CVs
tools/cv/build_cvs.py   turns content.py into the CV files (Word layout from tools/cv/template.docx)
cv-source/              editable .docx copies of the CVs (made by build_cvs.py, kept local, not published)
```

## Editing

**See it locally.** From the repository folder run `python -m http.server 8000`, then open <http://localhost:8000>.

**Change a text.** English is written directly in the HTML. Portuguese is in `assets/js/i18n/`, under the same key as the element's `data-i18n="…"` attribute. For example, `<p data-i18n="about.p1">…</p>` is `'about.p1': '…'` in `pt-data.js` or `pt-software.js`. Text that both sides share sits in `pt-common.js`. When you add a new text, give it a new `data-i18n` key and add the Portuguese line too.

**Add a job.** On each side, copy one `<article class="win quest">` block in the *Quest log* section and edit it. The current job also gets the `active` class and the *Active* label.

**Add a project.** Copy an `<article class="win item">` block in *Projects*. The big one at the top is `win feature`. The small one-line list at the end is *Foundations*.

**Update the CVs.** All four come from one file, so they always share the same layout. Edit the text in `tools/cv/content.py` (jobs, bullets, skills… in English and Portuguese), then run `python tools/cv/build_cvs.py`. It writes the PDFs the site links to, plus editable `.docx` copies in `cv-source/`. The PDF step uses Microsoft Word on Windows. Never name clients there: write "a client" (NDA). The site's `data-cv` links pick the file by language (`data-en="…"` / `data-pt="…"`), and `download.html` lists all four.

**Colours.** At the top of `pixel.css` (after the generated block) there are two theme blocks: `:root, .theme-soft` for red and `html[data-side="data"], .theme-data` for blue. Change the `--c1`, `--bar` and similar values there. The window frames, background tiles and scenery are small generated images: change their colours in `tools/pixel_art.py` and run `python tools/pixel_art.py`. That needs [Pillow](https://pypi.org/project/pillow/) for the icons and the preview image.

**Pixel icons.** Use `<span class="px-ic" data-px="disk"></span>`. Available: `monitor`, `chip`, `medal`, `cart`, `server`, `ship`, `mail`, `disk`, `book`. They're drawn letter by letter in `ICONS` inside `site.js`, so you can edit a row or add a new icon there.

**Patch notes (start page).** The panel at the bottom of the start page shows your GitHub contribution calendar (last 26 weeks), a level with an XP bar (XP = contributions in the last year, one level per 50) and your latest commits. It reads `assets/data/activity.json`, which a GitHub Action refreshes every day. To refresh it by hand, run `python tools/github_activity.py`, or start the *Update GitHub activity* workflow from the repository's Actions tab. Only public repositories appear.

**Contact form.** It posts to Formspree (`action="https://formspree.io/f/…"` on `#contact-form`). Messages carry a hidden `profile` field (`data` or `software`), so you know which side they came from.

**Before publishing**, run `python tools/check_site.py`. It should print `All good.`

### Building blocks (CSS classes)

| Class | What it is |
|---|---|
| `win` | pixel window (frame in the page's colour) |
| `win dialog` | dialog box; with `data-type` it types its text out |
| `sec-tab` | section title tab |
| `quest` (+ `active`) | one job in the quest log |
| `feature`, `item` | big / normal project card |
| `menu-list` | list where hovered items get the ▶ cursor |
| `pbtn` (+ `pbtn-main`, `pbtn-ghost`, `pbtn-sm`) | pixel buttons |
| `px-ic` | pixel icon container (see above) |
| `reveal` | appears as you scroll to it |

## Publishing

GitHub Pages serves the `main` branch as it is. Push and the site updates within a minute or two. If an old version still shows, do a hard refresh (Ctrl+F5). The empty `.nojekyll` file tells GitHub to serve the files untouched.

## Credits

Font: [Pixelify Sans](https://fonts.google.com/specimen/Pixelify+Sans) (SIL Open Font License), served by Google Fonts. All pixel art is drawn in code in this repository. The Avalon logo and pixel guardian appear only in the cards of the Avalon projects they belong to.
