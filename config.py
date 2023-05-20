import configparser
from os import path

from songbook2docx.styled.chord import HIDE_UNCOMMON_ADDED_INTERVAL, AUG_AND_DIM_GUITAR_MODE, DIVIDE_DELAYS, HIDE_INCOMPLETE_CHORDS, SIMPLIFY_MULTIPLY, SIMPLIFY_AUG_TO_GUITAR, HIDE_BASE

# DEFAULTS

TEMPLATE_PATH = "template/template.docx"
DEFAULT_FONT = "verdana"
wanted_font = DEFAULT_FONT
font_size = 9.0
show_author = True
tab_stops_offset = 0.5
INPUT_FILE_EXT = ".smm"
INITIAL_OPEN_PATH = path.expanduser("")

CONFIG: configparser.ConfigParser


def parse_config(filename) -> configparser.ConfigParser:
    global wanted_font, CONFIG, font_size, tab_stops_offset, show_author
    CONFIG = configparser.ConfigParser()
    CONFIG.read(filename)

    if "general" in CONFIG:
        general = CONFIG["general"]
        if "font-prefix" in general:
            wanted_font = "font-prefix"
        tab_stops_offset = get_as_float("tab-stops-offset", general, tab_stops_offset)

    if "style-song-content" in CONFIG:
        style_song_content = CONFIG["style-song-content"]
        font_size = get_as_float("font-size", style_song_content, font_size)

    return CONFIG


def get_chord_flags() -> int:
    flags = 0
    if "chord-flags" in CONFIG:
        chord_flags = CONFIG["chord-flags"]
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

    return flags


def get_wanted_font():
    return wanted_font


def get_font_size():
    return font_size


def get_show_authors():
    return font_size


def get_tab_stops_offset():
    return tab_stops_offset


def get_as_boolean(name, conf):
    if name in conf:
        return conf[name] == "yes"


def get_as_float(name, conf, default) -> float:
    if name in conf:
        try:
            return float(conf[name])
        except:
            pass
    return default