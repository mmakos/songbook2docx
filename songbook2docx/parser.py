import xml.etree.ElementTree as et

from songbook2docx.song import Song


def parse_html(html: str) -> list[Song]:
    html = html.replace("<br>", "<br/>")
    html = html.replace("""<meta charset="UTF-8">""", """<meta charset="UTF-8"/>""")
    html = html.replace("&emsp;", "<emsp/>")

    root = et.fromstring(html)

    body = root.find('body')
    songs = list()
    for song_div in body.findall("div"):
        s = Song(song_div)
        songs.append(s)
    return songs

