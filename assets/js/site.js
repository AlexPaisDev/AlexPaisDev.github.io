/* =====================================================================
   Alexandre Pais · behaviour shared by every page.
   Load it last, after the page's Portuguese strings (assets/js/i18n/*.js).

   What the HTML can ask for, through attributes:
     data-i18n="key"              swap this element's content for I18N_PT[key] in Portuguese
     data-i18n-attr="attr:key"    same for an attribute, e.g. "aria-label:menu" (separate several with ;)
     .lang [data-lang="en|pt"]    language buttons
     data-cv data-en=… data-pt=…  CV link; uses the PT file in Portuguese when there is one,
                                  otherwise keeps the EN file and fills its .cv-note with "(EN)"
     data-menu-toggle             button that opens/closes the element named in aria-controls
     data-spy                     nav whose #links get .active for the section on screen
     .reveal                      fades in when scrolled into view
     data-px="name"               draws a pixel icon from ICONS below (e.g. "disk", "medal")
     data-type + data-type-text   dialog box that types its text out
     canvas.guardian              the Avalon pixel guardian (only in the Avalon project cards)
     data-copy="text"             copies text; its [data-copy-label] says "Copied"
     #contact-form + #form-status Formspree form sent in the background
     #year                        filled with the current year
   ===================================================================== */
(() => {
  'use strict';
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch { } },
  };
  const root = document.documentElement;

  /* ---------------------------------------------------------------------
     LANGUAGE — English is the HTML source, Portuguese comes from I18N_PT
     --------------------------------------------------------------------- */
  const PT = window.I18N_PT || {};
  const original = new Map();
  const metaDesc = $('meta[name="description"]');
  const base = { title: document.title, desc: metaDesc ? metaDesc.content : '' };
  let lang = 'en';
  const listeners = [];
  const t = (key, en) => (lang === 'pt' && PT[key] != null ? PT[key] : en);

  function remember(el) {
    if (original.has(el)) return original.get(el);
    const rec = { html: el.hasAttribute('data-i18n') ? el.innerHTML : null, attrs: {} };
    (el.dataset.i18nAttr || '').split(';').filter(Boolean).forEach(pair => {
      const [attr] = pair.split(':');
      rec.attrs[attr] = el.getAttribute(attr);
    });
    original.set(el, rec);
    return rec;
  }

  function applyLang(next) {
    lang = next === 'pt' ? 'pt' : 'en';
    root.lang = lang === 'pt' ? 'pt-PT' : 'en';
    $$('[data-i18n], [data-i18n-attr]').forEach(el => {
      const rec = remember(el);
      if (el.hasAttribute('data-i18n')) el.innerHTML = t(el.dataset.i18n, rec.html);
      (el.dataset.i18nAttr || '').split(';').filter(Boolean).forEach(pair => {
        const [attr, key] = pair.split(':');
        el.setAttribute(attr, t(key, rec.attrs[attr]));
      });
    });
    document.title = t('meta.title', base.title);
    if (metaDesc) metaDesc.content = t('meta.desc', base.desc);
    $$('.lang [data-lang]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.lang === lang)));
    syncCv();
    listeners.forEach(fn => fn(lang));
  }

  /** CV links: data-en / data-pt hold the files; a page without a PT CV keeps the English one and says so. */
  function syncCv() {
    $$('[data-cv]').forEach(a => {
      const file = (lang === 'pt' && a.dataset.pt) || a.dataset.en;
      a.href = file;
      const note = $('.cv-note', a);
      if (note) note.textContent = lang === 'pt' && !a.dataset.pt ? ' (EN)' : '';
    });
  }

  $$('.lang [data-lang]').forEach(b => b.addEventListener('click', () => {
    applyLang(b.dataset.lang);
    store.set('lang', lang);
  }));

  const urlLang = new URLSearchParams(location.search).get('lang');
  const initial = urlLang || store.get('lang') || ((navigator.language || '').toLowerCase().startsWith('pt') ? 'pt' : 'en');
  applyLang(initial);

  /* ---------------------------------------------------------------------
     MENU (small screens) — any [data-menu-toggle] controls the element it names
     --------------------------------------------------------------------- */
  $$('[data-menu-toggle]').forEach(btn => {
    const menu = document.getElementById(btn.getAttribute('aria-controls'));
    if (!menu) return;
    const set = open => {
      menu.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', String(open));
    };
    btn.addEventListener('click', e => { e.stopPropagation(); set(!menu.classList.contains('open')); });
    menu.addEventListener('click', e => { if (e.target.closest('a')) set(false); });
    document.addEventListener('click', e => { if (menu.classList.contains('open') && !menu.contains(e.target)) set(false); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && menu.classList.contains('open')) { set(false); btn.focus(); } });
  });

  /* ---------------------------------------------------------------------
     ACTIVE SECTION in the nav / table of contents
     --------------------------------------------------------------------- */
  const spyLinks = $$('[data-spy] a[href^="#"]');
  if (spyLinks.length && 'IntersectionObserver' in window) {
    const byId = new Map();
    spyLinks.forEach(a => {
      const id = a.getAttribute('href').slice(1);
      if (!byId.has(id)) byId.set(id, []);
      byId.get(id).push(a);
    });
    const spy = new IntersectionObserver(entries => {
      entries.forEach(en => {
        if (!en.isIntersecting) return;
        spyLinks.forEach(a => a.classList.remove('active'));
        (byId.get(en.target.id) || []).forEach(a => a.classList.add('active'));
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    byId.forEach((_, id) => { const s = document.getElementById(id); if (s) spy.observe(s); });
  }

  /* ---------------------------------------------------------------------
     REVEAL ON SCROLL
     --------------------------------------------------------------------- */
  const revealEls = $$('.reveal');
  if (reduced || !('IntersectionObserver' in window)) {
    revealEls.forEach(el => el.classList.add('in'));
  } else {
    const io = new IntersectionObserver(entries => {
      entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -6% 0px', threshold: .06 });
    revealEls.forEach(el => io.observe(el));
  }

  /* ---------------------------------------------------------------------
     PIXEL ICONS — <span data-px="name"> becomes a crisp SVG sprite
     --------------------------------------------------------------------- */
  /* Colours, one letter each ('.' = transparent). */
  const PAL = {
    k: '#283038', w: '#f8f8f0', g: '#b0b8c0', y: '#f8c838', o: '#e08830', r: '#d85040',
    b: '#4878d8', c: '#68d0e0', t: '#2f8f86', l: '#7fd8c0', e: '#58d858', n: '#9a6a40',
  };
  /* Each icon is drawn row by row with the letters above. Edit a row to change the pixels;
     add a new entry to get a new icon for data-px="name". */
  const ICONS = {
    monitor: [
      '................',
      '.kkkkkkkkkkkkkk.',
      '.kggggggggggggk.',
      '.kgkkkkkkkkkkgk.',
      '.kgkttttttttkgk.',
      '.kgktlttttttkgk.',
      '.kgktwttttttkgk.',
      '.kgkttwtttttkgk.',
      '.kgktwtwwwttkgk.',
      '.kgkttttttttkgk.',
      '.kgkkkkkkkkkkgk.',
      '.kggggggggggegk.',
      '.kkkkkkkkkkkkkk.',
      '.....kggggk.....',
      '...kkkkkkkkkk...',
      '................',
    ],
    medal: [
      '.kbbk..kbbk.',
      '.kbbbkkbbbk.',
      '..kbbbbbbk..',
      '...kbbbbk...',
      '....kkkk....',
      '...kyyyyk...',
      '..kyywyyyk..',
      '..kywyyyyk..',
      '..kyyyyyok..',
      '..kyyyyook..',
      '...kyoook...',
      '....kkkk....',
    ],
    cart: [
      '.kkkkkkkkkk.',
      '.kggggggggk.',
      '.kgkkkkkkgk.',
      '.kgkbbbbkgk.',
      '.kgkbwbbkgk.',
      '.kgkbbbbkgk.',
      '.kgkkkkkkgk.',
      '.kggggggggk.',
      '.kgkgkgkggk.',
      '.kggggggggk.',
      '..kkkkkkkk..',
      '............',
    ],
    server: [
      '............',
      '.kkkkkkkkkk.',
      '.kggggggggk.',
      '.kgeegggbgk.',
      '.kggggggggk.',
      '.kkkkkkkkkk.',
      '.kggggggggk.',
      '.kgeegggbgk.',
      '.kggggggggk.',
      '.kkkkkkkkkk.',
      '....k..k....',
      '...kkkkkk...',
    ],
    ship: [
      '.....k......',
      '.....kk.....',
      '.....kwk....',
      '.....kwwk...',
      '.....kwwwk..',
      '.....kkkkkk.',
      'kkkkkkkkkkkk',
      '.krrrrrrrrk.',
      '..krrrrrrk..',
      '...kkkkkk...',
      'bbbbbbbbbbbb',
      '.b..b..b..b.',
    ],
    mail: [
      '............',
      '............',
      'kkkkkkkkkkkk',
      'kwkwwwwwwkwk',
      'kwwkwwwwkwwk',
      'kwwwkwwkwwwk',
      'kwwwwkkwwwwk',
      'kwwwwwwwwwwk',
      'kwwwwwwwwwwk',
      'kkkkkkkkkkkk',
      '............',
      '............',
    ],
    disk: [
      'kkkkkkkkkkk.',
      'kbkgggggkbbk',
      'kbkggkggkbbk',
      'kbkggkggkbbk',
      'kbkgggggkbbk',
      'kbbkkkkkbbbk',
      'kbbbbbbbbbbk',
      'kbkkkkkkkkbk',
      'kbkwwwwwwkbk',
      'kbkwkkkkwkbk',
      'kbkwwwwwwkbk',
      'kkkkkkkkkkkk',
    ],
    book: [
      '..kkkkkkkkk.',
      '.krrrrrrrrk.',
      '.krrwwwwrrk.',
      '.krrrrrrrrk.',
      '.krrwwwwrrk.',
      '.krrrrrrrrk.',
      '.krrrrrrrrk.',
      '.krrrrrrrrk.',
      '.kkkkkkkkkk.',
      '.kwwwwwwwwk.',
      '.kkkkkkkkkk.',
      '............',
    ],
    chip: [
      '....k..k....',
      '....k..k....',
      '..kkkkkkkk..',
      'kkkggggggkkk',
      '..kgccccgk..',
      '..kgcwccgk..',
      'kkkgccccgkkk',
      '..kggggggk..',
      '..kkkkkkkk..',
      '....k..k....',
      '....k..k....',
      '............',
    ],
  };
  function pixelSvg(rows) {
    const w = Math.max(...rows.map(r => r.length)), h = rows.length;
    let rects = '';
    rows.forEach((row, y) => [...row].forEach((ch, x) => {
      if (PAL[ch]) rects += `<rect x="${x}" y="${y}" width="1" height="1" fill="${PAL[ch]}"/>`;
    }));
    return `<svg viewBox="0 0 ${w} ${h}" shape-rendering="crispEdges" aria-hidden="true" focusable="false">${rects}</svg>`;
  }
  $$('[data-px]').forEach(el => { if (ICONS[el.dataset.px]) el.innerHTML = pixelSvg(ICONS[el.dataset.px]); });

  /* ---------------------------------------------------------------------
     TYPEWRITER — dialog boxes type their text, then show the ▼ prompt.
     The full text stays in the box (invisible) so its height never jumps;
     the typed copy is drawn on top of it. Click the box to skip.
     --------------------------------------------------------------------- */
  $$('[data-type]').forEach(box => {
    const target = $('[data-type-text]', box);
    if (!target) return;
    let timer = null;
    function run() {
      clearInterval(timer);
      const full = target.textContent;
      box.classList.remove('typed');
      if (reduced) { box.classList.add('typed'); return; }
      const ghost = Object.assign(document.createElement('span'), { className: 'tw-ghost', textContent: full });
      const live = Object.assign(document.createElement('span'), { className: 'tw-live' });
      ghost.setAttribute('aria-hidden', 'true');
      live.setAttribute('aria-hidden', 'true');
      target.setAttribute('aria-label', full);
      target.replaceChildren(ghost, live);
      const finish = () => { clearInterval(timer); target.textContent = full; box.classList.add('typed'); };
      let i = 0;
      timer = setInterval(() => {
        i += 2;
        live.textContent = full.slice(0, i);
        if (i >= full.length) finish();
      }, 28);
      box.onclick = finish;
    }
    listeners.push(run);
    run();
  });

  /* ---------------------------------------------------------------------
     THE PIXEL GUARDIAN — the mascot of the Avalon projects (shown only in their cards)
     --------------------------------------------------------------------- */
  function makeGuardian(cv) {
    const c = cv.getContext('2d');
    const W = cv.width, H = cv.height;
    const BODY = ['.......LGGG.......', '.......GGGD.......', '...LG..GGGD..GD...', '..LGGGGGGGGGGGGD..', '..GVVVVVVVVVVVVD..', '..GVVVVVVVVVVVVD..', 'LGGVVVVVVVVVVVVDGD', 'LGGVVVVVVVVVVVVDGD', 'LGGVVVVVVVVVVVVDGD', 'LGDDDDDDDDDDDDDDGD'];
    const SHIELD = ['YYYYYYY', 'YNNNNNY', 'YNNYNNY', 'YNYCYNY', '.YYYYY.', '..YNY..', '...Y...'];
    const C = { L: '#f7dc84', G: '#e6bd4e', D: '#b2892c', V: '#141230', Y: '#e6bd4e', N: '#1b1a45', C: '#62e6f0', legO: '#efcd68', legI: '#a47d29', cape: '#2c4196', capeD: '#22327a', blade: '#f2f8ff', edge: '#9fd3ff', grip: '#7a5520', eye: '#6fdca0', eyeHi: '#d8ffe9' };
    let f = 0, act = 'idle', tt = 0, sparks = [], timer = null;
    const px = (x, y, w, h, col) => { c.fillStyle = col; c.fillRect(Math.round(x), Math.round(y), w, h); };
    function draw() {
      c.clearRect(0, 0, W, H);
      const bx = 11; let by = 11, lift = 0;
      if (act === 'hop') by -= [0, 2, 3, 3, 2, 1, 0][Math.min(tt, 6)];
      else if (act === 'cheer') lift = tt < 3 ? tt : tt > 18 ? Math.max(0, 21 - tt) : 3;
      else if (f % 40 >= 20) by += 1;
      for (let r = 0; r < 13; r++) {
        const spread = Math.floor(r / 3), y = by + 4 + r, fl = act === 'idle' && r > 8 && (f + r) % 12 < 6 ? 1 : 0;
        px(bx + 1 - spread, y, 16 + spread * 2 + fl, 1, C.cape); px(bx + 15 + spread + fl, y, 2, 1, C.capeD);
      }
      [[3, 4], [6, 7], [10, 11], [13, 14]].forEach(([a, b], i) => { const l = act === 'hop' && tt > 0 && tt < 6 && i % 2 ? 1 : 0; px(bx + a, by + 10, 1, 3 - l, C.legO); px(bx + b, by + 10, 1, 3 - l, C.legI); });
      BODY.forEach((row, ry) => { for (let i = 0; i < row.length; i++) if (row[i] !== '.') px(bx + i, by + ry, 1, 1, C[row[i]]); });
      const blink = f % 47 < 2;
      [5, 11].forEach(a => { if (blink) { px(bx + a, by + 7, 2, 1, C.eye); return; } px(bx + a, by + 5, 2, 3, C.eye); px(bx + a, by + 5, 1, 1, C.eyeHi); });
      SHIELD.forEach((row, ry) => { for (let i = 0; i < row.length; i++) if (row[i] !== '.') px(bx - 7 + i, by + 5 + ry, 1, 1, C[row[i]]); });
      const sx = bx + 19, top = by - 8 - lift;
      px(sx, top + 1, 1, 13, C.blade); px(sx + 1, top + 1, 1, 13, C.edge); px(sx, top, 1, 1, C.blade);
      px(sx - 2, top + 14, 6, 1, C.G); px(sx, top + 15, 2, 3, C.grip); px(sx, top + 18, 2, 1, C.D);
      const g = f % 70; if (g < 12) { c.globalAlpha = .9; px(sx, top + 13 - g, 2, 1, '#fff'); c.globalAlpha = 1; }
      for (const s of sparks) { c.globalAlpha = Math.max(0, s.life / 14); px(s.x, s.y, 1, 1, s.col); if (s.life > 8) { px(s.x - 1, s.y, 1, 1, s.col); px(s.x + 1, s.y, 1, 1, s.col); px(s.x, s.y - 1, 1, 1, s.col); px(s.x, s.y + 1, 1, 1, s.col); } }
      c.globalAlpha = 1;
    }
    function step() { f++; tt++; if (act !== 'idle' && tt > (act === 'hop' ? 7 : 22)) { act = 'idle'; tt = 0; } sparks.forEach(s => { s.y -= .25; s.life--; }); sparks = sparks.filter(s => s.life > 0); draw(); }
    new IntersectionObserver(([en]) => {
      clearInterval(timer); timer = null;
      if (en.isIntersecting && !reduced) timer = setInterval(() => { if (!document.hidden) step(); }, 100);
    }).observe(cv);
    cv.addEventListener('click', e => {
      e.preventDefault(); e.stopPropagation();
      act = Math.random() < .5 ? 'hop' : 'cheer'; tt = 0;
      if (act === 'cheer') for (let i = 0; i < 6; i++) sparks.push({ x: 4 + Math.random() * 32, y: 4 + Math.random() * 14, life: 10 + Math.random() * 8, col: i % 2 ? '#f7dc84' : '#62e6f0' });
      if (!timer) for (let i = 0; i < 24; i++) setTimeout(step, i * 100);
    });
    draw();
  }
  $$('canvas.guardian').forEach(makeGuardian);

  /* ---------------------------------------------------------------------
     COPY EMAIL
     --------------------------------------------------------------------- */
  $$('[data-copy]').forEach(btn => btn.addEventListener('click', async () => {
    const label = $('[data-copy-label]', btn);
    try { await navigator.clipboard.writeText(btn.dataset.copy); }
    catch {
      const ta = Object.assign(document.createElement('textarea'), { value: btn.dataset.copy });
      document.body.append(ta); ta.select();
      try { document.execCommand('copy'); } catch { }
      ta.remove();
    }
    btn.classList.add('done');
    if (label) label.textContent = t('contact.copied', 'Copied');
    clearTimeout(btn._t);
    btn._t = setTimeout(() => { btn.classList.remove('done'); if (label) label.textContent = t('contact.copy', 'Copy'); }, 1800);
  }));

  /* ---------------------------------------------------------------------
     CONTACT FORM — Formspree, sent in the background
     --------------------------------------------------------------------- */
  const form = $('#contact-form'), status = $('#form-status');
  if (form && status) {
    const say = (key, en, cls) => { status.textContent = t(key, en); status.className = 'form-status' + (cls ? ' ' + cls : ''); };
    form.addEventListener('submit', async e => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      const btn = $('button[type="submit"]', form);
      btn.disabled = true;
      say('form.sending', 'Sending…');
      try {
        const res = await fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } });
        if (!res.ok) throw new Error(res.status);
        form.reset();
        say('form.ok', "Thanks! Your message is on its way. I'll reply soon.", 'ok');
      } catch {
        say('form.err', 'Something went wrong. Please email me directly at alexpaisdev@gmail.com.', 'err');
      } finally { btn.disabled = false; }
    });
  }

  /* ---------------------------------------------------------------------
     PATCH NOTES (start page) — GitHub activity from assets/data/activity.json
     (written by tools/github_activity.py). XP = contributions in the last year,
     one level every 50 XP.
     --------------------------------------------------------------------- */
  const notes = $('#notes');
  if (notes) {
    const XP_PER_LEVEL = 50;
    const level = n => (n === 0 ? 0 : n < 3 ? 1 : n < 6 ? 2 : n < 10 ? 3 : 4);
    const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);
    let data = null;
    function render() {
      const { stats, calendar, notes: list, updated } = data;
      $('#nt-year').textContent = stats.year;
      $('#nt-streak').textContent = stats.streak;
      $('#nt-days').textContent = stats.activeDays;
      $('#nt-lv').textContent = Math.floor(stats.year / XP_PER_LEVEL) + 1;
      $('#nt-xp').style.width = `${(stats.year % XP_PER_LEVEL) / XP_PER_LEVEL * 100}%`;
      $('#nt-xptxt').textContent = `${stats.year % XP_PER_LEVEL}/${XP_PER_LEVEL}`;
      $('#nt-updated').textContent = updated;
      const word = t('notes.contribs', 'contributions');
      const cal = $('#nt-cal');
      cal.setAttribute('aria-label', `${calendar.reduce((s, d) => s + d.count, 0)} ${word}, ${t('notes.weeks', 'last 26 weeks')}`);
      cal.innerHTML = calendar.map(d => `<i class="l${level(d.count)}" title="${d.date}: ${d.count} ${word}"></i>`).join('');
      $('#nt-list').innerHTML = list.slice(0, 4).map(n =>
        `<li><a href="${esc(n.url)}" target="_blank" rel="noopener"><span class="ver">v${n.date.slice(2).replace(/-/g, '.')}</span>` +
        `<b>${esc(n.repo)}</b><span class="msg">${esc(n.message)}</span></a></li>`).join('');
      notes.hidden = false;
    }
    fetch('assets/data/activity.json', { cache: 'no-cache' })
      .then(r => (r.ok ? r.json() : Promise.reject(r.status)))
      .then(d => { data = d; render(); listeners.push(render); })
      .catch(() => { /* no data: the panel just stays hidden */ });
  }

  const year = $('#year');
  if (year) year.textContent = new Date().getFullYear();
})();
