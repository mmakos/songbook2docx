from docx.text.run import Run
from fontTools.ttLib import TTFont

font_params: dict[str, tuple]
font_size: int = 9


def __get_font_params(path: str, prefix: str, suffix: str, default_pref) -> tuple:
    try:
        font = TTFont(f'{path}/{prefix}{suffix}.ttf')
    except:
        font = TTFont(f'{path}/{default_pref}{suffix}.ttf')

    cmap = font['cmap']
    t = cmap.getcmap(3, 1).cmap
    s = font.getGlyphSet()
    units_per_em = font['head'].unitsPerEm

    return t, s, units_per_em


def init_fonts(path: str, wanted_prefix: str, default_prefix: str, font_size_pt: int):
    global font_params, font_size
    font_params = {suffix: __get_font_params(path, wanted_prefix, suffix, default_prefix) for suffix in ("", "i", "b", "z")}
    font_size = font_size_pt


def __get_text_width(text: str, size: float, font: str):
    t, s, units_per_em = font_params[font]
    total = 0
    for c in text:
        if ord(c) in t and t[ord(c)] in s:
            total += s[t[ord(c)]].width
        else:
            total += s['.notdef'].width
    total = total * size / units_per_em
    return total


def get_text_width(runs: list[Run]) -> float:
    return sum((__get_text_width_for_run(run) for run in runs))


def __get_text_width_for_run(run: Run) -> float:
    font = ""
    if run.bold and run.italic:
        font = "z"
    elif run.italic:
        font = "i"
    elif run.bold:
        font = "b"

    size = float(font_size)
    if run.font.superscript or run.font.subscript:
        size = 2 * size / 3

    return __get_text_width(run.text, size, font)
