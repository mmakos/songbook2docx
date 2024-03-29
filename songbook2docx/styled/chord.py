import copy
import re

from songbook2docx.styled.transposition import up_transposition_dict, down_transposition_dict

addons_regex = r"( |(?<=[0-9](?=[0-9])))"

HIDE_UNCOMMON_ADDED_INTERVAL = 1
AUG_AND_DIM_GUITAR_MODE = 1 << 1
DIVIDE_DELAYS = 1 << 2
HIDE_INCOMPLETE_CHORDS = 1 << 3
SIMPLIFY_MULTIPLY = 1 << 4
SIMPLIFY_AUG_TO_GUITAR = 1 << 5
HIDE_BASE = 1 << 6
HIDE_ALTERNATIVE_KEY_FLAG = 1 << 7
HIDE_KEY_MARK_FLAG = 1 << 8


class Chord:
    def __init__(self, chord: str, aug: str, base: str, add: str, delimiter: str):
        self.chord: str = chord     # Fis, Ges itd
        self.aug: str = aug         # Rozszerzenie <, >
        self.base: str = base       # Podstawa 1, 3, 5
        self.add: str = add         # Dodane dźwięki 6, 7, 7<, 2 itd
        self.delimiter = delimiter

    @staticmethod
    def chord_from_text(text: str, delimiter: str):
        return Chord(Chord.__parse_chord(text),
                     Chord.__parse_aug(text),
                     Chord.__parse_base(text),
                     Chord.__parse_add(text),
                     delimiter)

    def is_same_chord(self, chord):
        return self.chord == chord.chord and self.aug == chord.aug and self.base == chord.base and self.add == chord.add

    @staticmethod
    def __parse_chord(text: str) -> str:
        match = re.search(r"[&<]", text)
        return text if match is None else text[:match.start()]

    @staticmethod
    def __parse_base(text: str) -> str:
        sub_start = text.find("<sub>")
        sub_end = text.find("</sub>")
        if sub_start >= 0 or sub_end >= 0:
            return text[sub_start + len("<sub>"): sub_end]
        return str()

    @staticmethod
    def __parse_add(text: str) -> str:
        sup_start = text.find("<sup>")
        sup_end = text.find("</sup>")
        if sup_start >= 0 or sup_end >= 0:
            return text[sup_start + len("<sup>"): sup_end].replace("&gt;", ">").replace("&lt;", "<")
        return str()

    @staticmethod
    def __parse_aug(text: str) -> str:
        index_start = text.find("<")
        index_start = index_start if index_start >= 0 else len(text)
        aug_start = text[:index_start].find("&")
        if aug_start >= 0:
            if text[aug_start:].startswith("&gt;"):
                return ">"
            elif text[aug_start:].startswith("&lt;"):
                return "<"
        if re.match(r"[a-zA-Z]+\*.*", text):
            return "*"
        return str()

    def apply_flags(self, flags: int) -> list['Chord']:
        if flags & HIDE_BASE > 0:
            self.base = ""
        if flags & SIMPLIFY_AUG_TO_GUITAR > 0:
            if self.aug == ">":
                self.add = "0"
            self.aug = ""
        addons = Chord.__apply_addons_flags(self.add, flags)
        chords = list()
        for i, addon in enumerate(addons):
            chord = copy.copy(self)
            if len(addons) > 1 and addon in ('1', '3', '5', '8'):
                chord.add = ''
            else:
                chord.add = addon
            chords.append(chord)
            if i < len(addons) - 1:
                chord.delimiter = " "
        return chords

    @staticmethod
    def __apply_addons_flags(addons: str, flags: int) -> list[str]:
        addons = addons.replace("-", "=")  # teraz opóżnienie będzie =, bo - może być dim
        parts = re.split(addons_regex, addons.strip())

        if flags & HIDE_UNCOMMON_ADDED_INTERVAL > 0:
            parts = [p for p in parts if not re.match("9|2>|7<|6>|4<", p)]

        if flags & HIDE_INCOMPLETE_CHORDS > 0:
            parts = [p for p in parts if "1" not in p and "5" not in p]

        if flags & AUG_AND_DIM_GUITAR_MODE > 0:
            for i, _ in enumerate(parts):
                temp = parts[i].replace(">", "-")
                temp = temp.replace("<", "+")
                parts[i] = temp

        if flags & SIMPLIFY_MULTIPLY > 0 and len(parts) > 1:
            parts = parts[-1:]

        if flags & DIVIDE_DELAYS:
            delays = [p.split("=") for p in parts if "=" in p]
            if len(delays) > 0:
                other = [p for p in parts if "=" not in p]
                max_delays = max([len(d) for d in delays])
                result = list()
                for i in range(max_delays):
                    temp = ["".join(other).strip()]
                    for d in delays:
                        if i < len(d):
                            temp.append(d[i])
                    result.append(temp)
                return [" ".join(r).strip().replace("=", "-") for r in result]

        return ["".join(parts).strip().replace("=", "-")]

    def transpose(self, interval: int):
        if interval == 0:
            return
        transpose_dict = up_transposition_dict if interval > 0 else down_transposition_dict
        for _ in range(interval):
            if self.chord.lower() in transpose_dict:
                is_dur = self.chord[0].isupper()
                self.chord = transpose_dict[self.chord.lower()]
                if is_dur:
                    self.chord = self.chord[0].upper() + self.chord[1:]
