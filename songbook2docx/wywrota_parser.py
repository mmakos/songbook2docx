import re
from html.parser import HTMLParser
import xml.etree.ElementTree as et

from songbook2docx.song import Row, Song
from songbook2docx.styled.chord import Chord
from songbook2docx.styled.chords import Chords
from songbook2docx.styled.song_text import SongText

TEXT = 0
CHORDS = 1


class WywrotaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text: list[list] = [[str(), list()]]
        self.mode = TEXT

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "span":
            self.mode = TEXT
        elif tag == "code":
            self.mode = CHORDS
        elif tag == "br":
            self.text.append([str(), list()])

    def handle_endtag(self, tag: str) -> None:
        if tag == "span":
            self.mode = TEXT
        elif tag == "code":
            self.mode = TEXT

    def handle_data(self, data: str) -> None:
        if self.mode == TEXT:
            self.text[-1][0] += data
        elif self.mode == CHORDS:
            self.text[-1][1].append(data)

    @staticmethod
    def parse_wywrota_html(html: str):
        parser = WywrotaParser()
        parser.feed(html)
        indexes_to_remove = list()
        for i in range(len(parser.text) - 1):
            text0 = parser.text[i]
            text1 = parser.text[i + 1]
            if len(text0[0].strip()) == 0 and len(text0[1]) == 0 and len(text1[0].strip()) == 0 and len(text1[1]) == 0:
                indexes_to_remove.insert(0, i)
        for index_to_remove in indexes_to_remove:
            parser.text.pop(index_to_remove)
        return parser.text

    @staticmethod
    def parse_single_chord(chord_text: str, is_last=False) -> Chord:
        chord = chord_text.split("/")[0]
        chord = chord.replace("sus", "")
        chord_split = re.split(r"([0-9]+)", chord)
        chord = chord_split[0]
        add = chord_split[1] if len(chord_split) > 1 else str()
        delimiter = str() if is_last else " "
        return Chord(chord, str(), str(), add, delimiter)

    @staticmethod
    def parse_chords(chords_list: list[str]) -> Chords:
        return Chords([WywrotaParser.parse_single_chord(chord, i == len(chords_list) - 1) for i, chord in enumerate(chords_list)], None, 0)

    @staticmethod
    def parse_row(line: list) -> Row:
        return Row([SongText(line[0].strip()), WywrotaParser.parse_chords(line[1])])

    @staticmethod
    def parse(html: et.Element) -> Song:
        song = Song()
        song.rows = [WywrotaParser.parse_row(line) for line in WywrotaParser.parse_wywrota_html(et.tostring(html.find("song"), encoding="unicode")[len("<song>"):-len("</song>")])]
        song.parse_options(html)
        return song
