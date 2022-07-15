from html.parser import HTMLParser

from docx.text.run import Run


class Styler(HTMLParser):
    BOLD = 0b1
    ITALIC = 0b10
    UNDERLINE = 0b100
    STRIKE = 0b1000
    SUPER = 0b10000
    SUB = 0b100000

    def __init__(self):
        super().__init__()
        self.current_style: dict[str, int] = {
            "b": 0, "i": 0, "u": 0, "s": 0, "sup": 0, "sub": 0,
        }
        self.runs: list[tuple[str, int]] = list()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in self.current_style:
            self.current_style[tag] = self.current_style[tag] + 1

    def handle_endtag(self, tag: str) -> None:
        if tag in self.current_style:
            self.current_style[tag] = self.current_style[tag] - 1

    def handle_data(self, data: str) -> None:
        styles = 0
        if self.current_style["b"] > 0:
            styles |= Styler.BOLD
        if self.current_style["i"] > 0:
            styles |= Styler.ITALIC
        if self.current_style["u"] > 0:
            styles |= Styler.UNDERLINE
        if self.current_style["s"] > 0:
            styles |= Styler.STRIKE
        if self.current_style["sup"] > 0:
            styles |= Styler.SUPER
        if self.current_style["sub"] > 0:
            styles |= Styler.SUB

        self.runs.append((data, styles))

    @staticmethod
    def style_text(html: str) -> list[tuple[str, int]]:
        parser = Styler()
        parser.feed(html)
        return parser.runs

    @staticmethod
    def style_run(run: Run, style: int):
        if style & Styler.BOLD > 0:
            run.bold = True
        if style & Styler.ITALIC > 0:
            run.italic = True
        if style & Styler.UNDERLINE > 0:
            run.underline = True
        if style & Styler.STRIKE > 0:
            run.font.strike = True
        if style & Styler.SUPER > 0:
            run.font.superscript = True
        if style & Styler.SUB > 0:
            run.font.subscript = True

