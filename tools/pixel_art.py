"""
Regenerates the site's pixel art.

  python tools/pixel_art.py

1. Rewrites the GENERATED block at the top of assets/css/pixel.css:
   window frames, background tiles, the scenery strips (waves / mountains)
   and the ▶ / ▼ cursor shapes, all as small inline SVGs.
2. Redraws assets/img/favicon.svg, apple-touch-icon.png and og-image.png
   (the link-preview picture). This part needs Pillow:  pip install pillow

Change a colour or a shape below, run the script, and refresh the page.
"""
import math
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
CSS = ROOT / 'assets' / 'css' / 'pixel.css'
IMG = ROOT / 'assets' / 'img'

INK, WHITE = '#283038', '#f8f8f0'
# theme colours (keep in sync with the variables in pixel.css)
RED, RED_LIGHT, AMBER, AMBER_LIGHT = '#d84a3a', '#f4a08a', '#f0a030', '#f8d488'
BLUE, BLUE_LIGHT, CYAN, CYAN_LIGHT = '#3a78d8', '#98c0f4', '#38b8d8', '#a8e4f0'
GREY, GREY_LIGHT = '#b8bcc4', '#e0e2e6'
TILE_RED = ('#f7dccb', '#f2cfb9')
TILE_BLUE = ('#d3e5f8', '#c6dcf4')

# mountain profile (x, height) and wave shape, shared by the CSS strip and the preview image
PEAKS = [(0, 5), (10, 14), (20, 6), (31, 11), (40, 7), (44, 9), (48, 5)]
WAVE = lambda x, period: round(4 + 2.4 * math.sin(2 * math.pi * x / period))


# ---------------------------------------------------------------- CSS pieces
def uri(svg):
    """Inline SVG as a CSS url(), escaped the way browsers like it."""
    return "url(\"data:image/svg+xml," + svg.replace('"', "'").replace('#', '%23').replace('<', '%3C').replace('>', '%3E') + "\")"


def svg(w, h, body):
    return f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}' viewBox='0 0 {w} {h}' shape-rendering='crispEdges'>{body}</svg>"


def runs(cells):
    """{colour: [(x, y), …]} -> <path>s, merging horizontal runs of pixels."""
    out = []
    for col, pts in cells.items():
        pts = sorted(set(pts), key=lambda p: (p[1], p[0]))
        d, i = '', 0
        while i < len(pts):
            x, y = pts[i]
            w = 1
            while i + w < len(pts) and pts[i + w] == (x + w, y):
                w += 1
            d += f'M{x} {y}h{w}v1h-{w}z'
            i += w
        out.append(f"<path fill='{col}' d='{d}'/>")
    return ''.join(out)


def frame(band, light):
    """7x7 window frame used with `border-image: … 3 fill / 9px`: outline, colour band, light line, white middle."""
    return uri(svg(7, 7,
                   f"<path fill='{INK}' d='M1 0h5v1H1zM0 1h1v5H0zM6 1h1v5H6zM1 6h5v1H1z'/>"
                   f"<path fill='{band}' d='M1 1h5v5H1z'/><path fill='{light}' d='M2 2h3v3H2z'/><path fill='{WHITE}' d='M3 3h1v1H3z'/>"))


def stripes(a, b):
    """8x8 tile of diagonal stripes, the page background."""
    rows = ['M0 0h4v1H0z', 'M1 1h4v1H1z', 'M2 2h4v1H2z', 'M3 3h4v1H3z', 'M4 4h4v1H4z',
            'M5 5h3v1H5zM0 5h1v1H0z', 'M6 6h2v1H6zM0 6h2v1H0z', 'M7 7h1v1H7zM0 7h3v1H0z']
    return uri(svg(8, 8, f"<rect width='8' height='8' fill='{a}'/><path fill='{b}' d='{''.join(rows)}'/>"))


def waves():
    W, H = 32, 12
    cells = {'#e8f4ff': [], '#5a98e8': [], '#2c5aa8': [], '#20468a': []}
    for x in range(W):
        top = WAVE(x, W)
        cells['#e8f4ff'].append((x, top))
        cells['#5a98e8'].append((x, top + 1))
        for y in range(top + 2, H):
            cells['#2c5aa8' if y < H - 3 else '#20468a'].append((x, y))
    cells['#5a98e8'] += [(6, 9), (7, 9), (21, 10), (22, 10), (27, 8)]
    return uri(svg(W, H, runs(cells)))


def mountain_height(x, peaks):
    for (x0, h0), (x1, h1) in zip(peaks, peaks[1:]):
        if x0 <= x <= x1:
            return round(h0 + (h1 - h0) * (x - x0) / (x1 - x0)), h1 >= h0
    return peaks[-1][1], False


def mountains():
    W, H = 48, 16
    cells = {'#f08a64': [], '#c8503c': [], '#9a3a2e': [], '#7a2a24': []}
    for x in range(W):
        h, rising = mountain_height(x, PEAKS)
        top = H - h
        cells['#f08a64' if rising else '#c8503c'].append((x, top))
        for y in range(top + 1, H):
            cells['#7a2a24' if y >= H - 3 else ('#c8503c' if rising else '#9a3a2e')].append((x, y))
    return uri(svg(W, H, runs(cells)))


def css_block():
    arrow = uri(svg(5, 7, "<path d='M0 0h1v7H0zM1 1h1v5H1zM2 2h1v3H2zM3 3h1v1H3z'/>"))
    down = uri(svg(7, 4, "<path d='M0 0h7v1H0zM1 1h5v1H1zM2 2h3v1H2zM3 3h1v1H3z'/>"))
    lines = {
        '--frame-ruby': frame(RED, RED_LIGHT),
        '--frame-ruby-alt': frame(AMBER, AMBER_LIGHT),
        '--frame-sapph': frame(BLUE, BLUE_LIGHT),
        '--frame-sapph-alt': frame(CYAN, CYAN_LIGHT),
        '--frame-plain': frame(GREY, GREY_LIGHT),
        '--tile-ruby': stripes(*TILE_RED),
        '--tile-sapph': stripes(*TILE_BLUE),
        '--scene-sapph': waves(),
        '--scene-ruby': mountains(),
        '--px-arrow': arrow,
        '--px-down': down,
    }
    return ':root {\n' + ''.join(f'  {k}: {v};\n' for k, v in lines.items()) + '}'


def write_css():
    text = CSS.read_text(encoding='utf8')
    start, end = '/* GENERATED:START', '/* GENERATED:END */'
    a, b = text.index(start), text.index(end)
    head = text[a:text.index('*/', a) + 2]
    text = text[:a] + head + '\n' + css_block() + '\n' + text[b:]
    CSS.write_text(text, encoding='utf8')
    print('updated', CSS.relative_to(ROOT))


# ---------------------------------------------------------------- images
def write_images():
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print('Pillow not installed: skipped favicon / og-image (pip install pillow)')
        return
    rgb = lambda h: tuple(int(h.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))

    # favicon: 16x16, blue half with "A", red half with "P"
    A = ['.###.', '#...#', '#...#', '#####', '#...#', '#...#', '#...#']
    P = ['####.', '#...#', '#...#', '####.', '#....', '#....', '#....']
    px = [[None] * 16 for _ in range(16)]
    for y in range(16):
        for x in range(16):
            if x in (0, 15) and y in (0, 15):
                continue
            px[y][x] = INK if x in (0, 15) or y in (0, 15) else (BLUE if x < 8 else RED)
    for glyph, ox in ((A, 2), (P, 9)):
        for gy, row in enumerate(glyph):
            for gx, ch in enumerate(row):
                if ch == '#':
                    px[4 + gy][ox + gx] = WHITE
    for y in range(15, 0, -1):          # GBA-style text shadow
        for x in range(15, 0, -1):
            if px[y][x] in (BLUE, RED) and px[y - 1][x - 1] == WHITE:
                px[y][x] = '#24509c' if x < 8 else '#9c3026'
    rects = ''.join(f"<rect x='{x}' y='{y}' width='1' height='1' fill='{c}'/>" for y, row in enumerate(px) for x, c in enumerate(row) if c)
    (IMG / 'favicon.svg').write_text(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' shape-rendering='crispEdges'>{rects}</svg>\n")
    small = Image.new('RGB', (16, 16), rgb(INK))
    for y, row in enumerate(px):
        for x, c in enumerate(row):
            if c:
                small.putpixel((x, y), rgb(c))
    touch = Image.new('RGB', (180, 180), rgb(INK))
    touch.paste(small.resize((176, 176), Image.NEAREST), (2, 2))
    touch.save(IMG / 'apple-touch-icon.png', optimize=True)

    # og-image: drawn at 300x158 then scaled x4 with hard pixels -> 1200x630
    W, H = 300, 158
    img = Image.new('RGB', (W, H))
    d = ImageDraw.Draw(img)
    for y in range(H):
        for x in range(W):
            a, b = TILE_BLUE if x < 150 else TILE_RED
            img.putpixel((x, y), rgb(b) if (x - y) % 8 < 4 else rgb(a))
    for x in range(150):                                   # waves
        top = H - 12 + WAVE(x, 32)
        img.putpixel((x, top), rgb('#e8f4ff'))
        img.putpixel((x, top + 1), rgb('#5a98e8'))
        for y in range(top + 2, H):
            img.putpixel((x, y), rgb('#2c5aa8' if y < H - 3 else '#20468a'))
    big_peaks = [(150, 5), (168, 15), (186, 7), (206, 12), (226, 6), (250, 16), (272, 8), (300, 11)]
    for x in range(150, W):                                # mountains
        h, rising = mountain_height(x, big_peaks)
        top = H - h
        img.putpixel((x, top), rgb('#f08a64' if rising else '#c8503c'))
        for y in range(top + 1, H):
            img.putpixel((x, y), rgb('#7a2a24' if y >= H - 3 else ('#c8503c' if rising else '#9a3a2e')))
    d.rectangle([149, 0, 150, H], fill=rgb(INK))

    x0, y0, x1, y1 = 46, 22, 254, 116                      # centre window
    d.rectangle([x0 + 1, y0, x1 - 1, y1], fill=rgb(INK))
    d.rectangle([x0, y0 + 1, x1, y1 - 1], fill=rgb(INK))
    d.rectangle([x0 + 1, y0 + 1, x1 - 1, y1 - 1], fill=rgb(GREY))
    d.rectangle([x0 + 2, y0 + 2, x1 - 2, y1 - 2], fill=rgb(GREY_LIGHT))
    d.rectangle([x0 + 3, y0 + 3, x1 - 3, y1 - 3], fill=rgb(WHITE))
    d.rectangle([x0 + 4, y1 + 1, x1 + 1, y1 + 2], fill=(150, 150, 150))
    d.rectangle([x1 + 1, y0 + 4, x1 + 2, y1 + 2], fill=(150, 150, 150))

    font = ImageFont.load_default_imagefont()               # Pillow's built-in bitmap font

    def text(s, x, y, col, scale=1, center=False):
        mask = Image.new('L', (round(font.getlength(s)) + 1, 13), 0)
        ImageDraw.Draw(mask).text((0, 0), s, font=font, fill=255)
        if scale > 1:
            mask = mask.resize((mask.width * scale, mask.height * scale), Image.NEAREST)
        if center:
            x = round(x - mask.width / 2)
        img.paste(rgb('#d6d2c6'), (x + scale, y + scale), mask)
        img.paste(rgb(col), (x, y), mask)
        return mask.width

    text('ALEXANDRE PAIS', 150, 32, INK, scale=2, center=True)
    x = 150 - round(font.getlength('DATA ENGINEER / SOFTWARE ENGINEER') / 2)
    x += text('DATA ENGINEER', x, 64, BLUE)
    x += text(' / ', x, 64, '#5d636d')
    text('SOFTWARE ENGINEER', x, 64, RED)
    text('LISBON - OPEN TO ROLES IN ASIA', 150, 80, '#5d636d', center=True)
    text('alexpaisdev.github.io', 150, 98, INK, center=True)

    pal = {'k': INK, 'w': WHITE, 'g': '#b0b8c0', 'c': '#68d0e0', 't': '#2f8f86', 'l': '#7fd8c0', 'e': '#58d858'}
    chip = ['....k..k....', '....k..k....', '..kkkkkkkk..', 'kkkggggggkkk', '..kgccccgk..', '..kgcwccgk..',
            'kkkgccccgkkk', '..kggggggk..', '..kkkkkkkk..', '....k..k....', '....k..k....']
    monitor = ['.kkkkkkkkkkkkkk.', '.kggggggggggggk.', '.kgkkkkkkkkkkgk.', '.kgkttttttttkgk.', '.kgktlttttttkgk.',
               '.kgktwttttttkgk.', '.kgkttwtttttkgk.', '.kgktwtwwwttkgk.', '.kgkttttttttkgk.', '.kgkkkkkkkkkkgk.',
               '.kggggggggggegk.', '.kkkkkkkkkkkkkk.', '.....kggggk.....', '...kkkkkkkkkk...']
    for rows, ox, oy in ((chip, 12, 56), (monitor, 262, 52)):
        for y, row in enumerate(rows):
            for x, ch in enumerate(row):
                if ch in pal:
                    d.rectangle([ox + x * 2, oy + y * 2, ox + x * 2 + 1, oy + y * 2 + 1], fill=rgb(pal[ch]))
    img.resize((1200, 632), Image.NEAREST).crop((0, 1, 1200, 631)).save(IMG / 'og-image.png', optimize=True)
    print('updated assets/img/favicon.svg, apple-touch-icon.png, og-image.png')


if __name__ == '__main__':
    write_css()
    write_images()
