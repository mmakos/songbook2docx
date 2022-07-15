from docx.shared import Cm
from docx.text.paragraph import Paragraph
from docx.text.run import Run

from songbook2docx.styled.styled_cell import StyledCell
from songbook2docx.utils.styler import Styler


class SongText(StyledCell):
    def __init__(self, html: str):
        self.runs: list[tuple[str, int]] = Styler.style_text(html)

    def add_runs_to_paragraph(self, par: Paragraph) -> list[Run]:
        indents = 0
        runs = list()
        if len(self.runs) > 0:
            first_text = self.runs[0][0]
            indents = SongText.__get_indents(first_text)
            if indents > 0:
                par.paragraph_format.left_indent = Cm(indents * 0.75)
        for r in self.runs:
            run = par.add_run(r[0][indents:])
            Styler.style_run(run, r[1])
            runs.append(run)

        return runs

    @staticmethod
    def __get_indents(text: str) -> int:
        indents = 0
        for c in text:
            if c == '\t':
                indents += 1
        return indents
