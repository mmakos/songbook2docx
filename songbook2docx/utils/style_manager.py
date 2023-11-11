from docx import Document
from docx.shared import Pt
from docx.styles.style import BaseStyle

TITLE = "Tytuł piosenki"
AUTHOR = "Autor piosenki"
SONG_TEXT = "Treść piosenki"
REPETITION = "Powtórzenia"
CHORDS = "Akordy"
KEY = "Tonacja"
SONG = "Piosenka"


def set_font_bold(font, conf):
    if "font-bold" in conf:
        font_bold = conf["font-bold"]
        if font_bold in ("yes", "no"):
            font.bold = font_bold == "yes"


def set_font_italic(font, conf):
    if "font-italic" in conf:
        font_italic = conf["font-italic"]
        if font_italic in ("yes", "no"):
            font.italic = font_italic == "yes"


class StyleManager:
    def __init__(self, doc: Document, config: dict):
        self.document = doc
        self.__parse_config_styles(config)

    def get_style(self, style: str) -> BaseStyle | None:
        if self.document is not None and style in self.document.styles:
            return self.document.styles[style]
        else:
            return None

    def __parse_config_styles(self, config: dict):
        song_style = self.get_style(SONG_TEXT)
        chords_style = self.get_style(CHORDS)
        repetition_style = self.get_style(REPETITION)
        key_style = self.get_style(KEY)
        if "style-song-content" in config:
            style_song_content = config["style-song-content"]
            if "font-size" in style_song_content:
                try:
                    font_size = float(style_song_content["font-size"])
                    font_size_length = Pt(font_size)
                    song_style.font.size = font_size_length
                    chords_style.font.size = font_size_length
                    repetition_style.font.size = font_size_length
                    key_style.font.size = font_size_length
                except:
                    pass
            if "font-name" in style_song_content:
                font_name = style_song_content["font-name"]
                song_style.font.name = font_name
                chords_style.font.name = font_name
                repetition_style.font.name = font_name
                key_style.font.name = font_name
            set_font_bold(song_style.font, style_song_content)
            set_font_italic(song_style.font, style_song_content)

        if "style-chords" in config:
            style_chords = config["style-chords"]
            set_font_bold(chords_style.font, style_chords)
            set_font_italic(chords_style.font, style_chords)

        if "style-repetition" in config:
            style_repetition = config["style-repetition"]
            set_font_bold(repetition_style.font, style_repetition)
            set_font_italic(repetition_style.font, style_repetition)

        if "style-key" in config:
            style_key = config["style-key"]
            set_font_bold(key_style.font, style_key)
            set_font_italic(key_style.font, style_key)
