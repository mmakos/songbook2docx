from docx.text.run import Run
from fontTools.ttLib import TTFont


class TextWidthProvider:
    def __init__(self, path: str, wanted_prefix: str, default_prefix: str, font_size_pt: int):
        self.font_params = {suffix: self.__get_font_params(path, wanted_prefix, suffix, default_prefix) for suffix in ("", "i", "b", "z")}
        self.font_size = font_size_pt

    def get_text_width(self, runs: list[Run]) -> float:
        return sum((self.__get_text_width_for_run(run) for run in runs))

    @staticmethod
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

    def __get_text_width(self, text: str, size: float, font: str):
        t, s, units_per_em = self.font_params[font]
        total = 0
        for c in text:
            if ord(c) in t and t[ord(c)] in s:
                total += s[t[ord(c)]].width
            else:
                total += s['.notdef'].width
        total = total * size / units_per_em
        return total

    def __get_text_width_for_run(self, run: Run) -> float:
        font = ""
        if (run.bold or run.style.font.bold) and (run.italic or run.style.font.italic):
            font = "z"
        elif run.italic or run.style.font.italic:
            font = "i"
        elif run.bold or run.style.font.bold:
            font = "b"

        size = float(self.font_size)
        if run.font.superscript or run.font.subscript:
            size = 2 * size / 3

        return self.__get_text_width(run.text, size, font)
