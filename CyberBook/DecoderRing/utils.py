from string import ascii_letters


def ascii_to_index(letter: str) -> int:
    return ord(letter.lower()) - 97


def index_to_ascii(index: int, capitalize: bool = False) -> str:
    index = index % 26
    if capitalize:
        return chr(index + 65)
    return chr(index + 97)


def is_ascii_letter(character: str) -> bool:
    return character in ascii_letters


def is_not_ascii_letter(character: str) -> bool:
    return character not in ascii_letters
