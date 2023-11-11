from docx.text.paragraph import Paragraph

from songbook2docx.styled.styled_cell import StyledCell
from songbook2docx.utils.style_manager import StyleManager, REPETITION


class Repetition(StyledCell):
    def __init__(self, html: str):
        self.text = Repetition.__parse_html(html)

    @staticmethod
    def __parse_html(html: str) -> str:
        html = html.replace("<b>", "")
        html = html.replace("</b>", "")
        return html

    def add_runs_to_paragraph(self, par: Paragraph, style_manager: StyleManager):
        run = par.add_run(self.text if self.text else None, style=style_manager.get_style(REPETITION))
        return [run]
