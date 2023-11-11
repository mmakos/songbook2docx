import configparser
from os import path

from songbook2docx.styled.chord import HIDE_UNCOMMON_ADDED_INTERVAL, AUG_AND_DIM_GUITAR_MODE, DIVIDE_DELAYS, \
    HIDE_INCOMPLETE_CHORDS, SIMPLIFY_MULTIPLY, SIMPLIFY_AUG_TO_GUITAR, HIDE_BASE, HIDE_ALTERNATIVE_KEY_FLAG, HIDE_KEY_MARK_FLAG

# DEFAULTS

TEMPLATE_PATH = "template/template.docx"
DEFAULT_FONT = "verdana"
INPUT_FILE_EXT = ".smm"
INITIAL_OPEN_PATH = path.expanduser("")

CONFIG: dict


class Config:
    def __init__(self, config: dict):
        self.wanted_font = DEFAULT_FONT
        self.font_size = 9.0
        self.show_author = True
        self.tab_stops_offset = 0.5
        self.config = config
        self.parse_main_cfg(config)

    def parse_main_cfg(self, dictionary: dict):
        if "general" in dictionary:
            general = dictionary["general"]
            if "font-family" in general:
                self.wanted_font = general["font-family"].lower()
            if "show-author" in general:
                self.show_author = get_as_boolean("show-author", general)
            self.tab_stops_offset = get_as_float("tab-stops-offset", general, self.tab_stops_offset)

        if "style-song-content" in dictionary:
            style_song_content = dictionary["style-song-content"]
            self.font_size = get_as_float("font-size", style_song_content, self.font_size)

    def get_chord_flags(self) -> int:
        flags = 0
        if "chord-flags" in self.config:
            chord_flags = self.config["chord-flags"]
            if get_as_boolean("hide-uncommon-added-interval", chord_flags):
                flags |= HIDE_UNCOMMON_ADDED_INTERVAL
            if get_as_boolean("aug-and-dim-guitar-mode", chord_flags):
                flags |= AUG_AND_DIM_GUITAR_MODE
            if get_as_boolean("divide-delays", chord_flags):
                flags |= DIVIDE_DELAYS
            if get_as_boolean("hide-incomplete-chords", chord_flags):
                flags |= HIDE_INCOMPLETE_CHORDS
            if get_as_boolean("simplify-multiply", chord_flags):
                flags |= SIMPLIFY_MULTIPLY
            if get_as_boolean("simplify-aug-to-guitar", chord_flags):
                flags |= SIMPLIFY_AUG_TO_GUITAR
            if get_as_boolean("hide-base", chord_flags):
                flags |= HIDE_BASE
            if get_as_boolean("hide-alternative-key-flag", chord_flags):
                flags |= HIDE_ALTERNATIVE_KEY_FLAG
            if get_as_boolean("hide-key-mark-flag", chord_flags):
                flags |= HIDE_KEY_MARK_FLAG

        return flags


def parse_config(filename) -> dict:
    config = configparser.ConfigParser()
    config.read(filename)
    return {s: dict(config.items(s)) for s in config.sections()}


def get_as_boolean(name, conf):
    if name in conf:
        return conf[name] == "yes"
    return False


def get_as_float(name, conf, default) -> float:
    if name in conf:
        try:
            return float(conf[name])
        except:
            pass
    return default
