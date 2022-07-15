from configparser import ConfigParser

from docx import Document
from docx.shared import Pt
from docx.styles.style import BaseStyle

document: Document

TITLE = "Tytuł piosenki"
AUTHOR = "Autor piosenki"
SONG = "Treść piosenki"
REPETITION = "Powtórzenia"
CHORDS = "Akordy"
KEY = "Tonacja"


def init(doc: Document, config: ConfigParser):
    global document
    document = doc
    __parse_config_styles(config)


def get_style(style: str) -> BaseStyle | None:
    if document is not None and style in document.styles:
        return document.styles[style]
    else:
        return None


def __parse_config_styles(config: ConfigParser):
    song_style = get_style(SONG)
    chords_style = get_style(CHORDS)
    repetition_style = get_style(REPETITION)
    key_style = get_style(KEY)
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
        __set_font_bold(song_style.font, style_song_content)
        __set_font_italic(song_style.font, style_song_content)

    if "style-chords" in config:
        style_chords = config["style-chords"]
        __set_font_bold(chords_style.font, style_chords)
        __set_font_italic(chords_style.font, style_chords)

    if "style-repetition" in config:
        style_repetition = config["style-repetition"]
        __set_font_bold(repetition_style.font, style_repetition)
        __set_font_italic(repetition_style.font, style_repetition)

    if "style-key" in config:
        style_key = config["style-key"]
        __set_font_bold(key_style.font, style_key)
        __set_font_italic(key_style.font, style_key)


def __set_font_bold(font, conf):
    if "font-bold" in conf:
        font_bold = conf["font-bold"]
        if font_bold in ("yes", "no"):
            font.bold = font_bold == "yes"


def __set_font_italic(font, conf):
    if "font-italic" in conf:
        font_italic = conf["font-italic"]
        if font_italic in ("yes", "no"):
            font.italic = font_italic == "yes"
