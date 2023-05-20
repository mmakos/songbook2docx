import xml.etree.ElementTree as et

from songbook2docx.song import Song
from songbook2docx.wywrota_parser import WywrotaParser


def parse_html(html: str) -> list[Song]:
    html = html.replace("<br>", "<br/>").replace("&emsp;", "<emsp/>").replace("&nbsp;", "<nbsp/>").replace(" ", " ")

    root = et.fromstring(html)

    body = root.find('body')
    songs = list()
    for song_div in body.findall("div"):
        if song_div.attrib.get("songbook") == "wywrota":
            song = WywrotaParser.parse(song_div)
            songs.append(song)
        else:
            songs.append(Song(song_div))
    return songs

