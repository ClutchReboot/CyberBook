from base64 import urlsafe_b64decode, urlsafe_b64encode
from html import escape, unescape
from . import utils


import hashlib
import urllib.parse


def caeser(data, shift: int = 5, decode: bool = False) -> str:
    """
    Caeser's Cipher used on a string.
    """

    if decode:
        shift = -shift

    result = ""

    for char in data:
        if utils.is_not_ascii_letter(character=char):  # Account for spaces and special chars.
            result += char
        elif char.isupper():
            enciphered_index = (utils.ascii_to_index(letter=char) + shift) % 26
            result += utils.index_to_ascii(index=enciphered_index, capitalize=True)
        else:
            enciphered_index = (utils.ascii_to_index(letter=char) + shift) % 26
            result += utils.index_to_ascii(index=enciphered_index)
    return result


def base64(data: str, decode: bool = False) -> str:
    """
    By default, encode into Base64 string.
    """

    if decode:
        return urlsafe_b64decode(data).decode()

    encoded = urlsafe_b64encode(data.encode('utf-8'))
    return encoded.decode()


def full_url(data: str, decode: bool = False) -> str:

    if decode:
        url_decoded = data.replace('%2E', '.')
        return urllib.parse.unquote(url_decoded)

    url_encode = urllib.parse.quote(data)
    return url_encode.replace('.', '%2E')


def basic_hex(data, decode: bool = False) -> str:
    """
    By default, encode into Hexadecimal string.
    """
    if decode:
        return bytes.fromhex(data).decode()

    bytes_conversion = data.encode()
    return bytes_conversion.hex()


def html(data, decode: bool = False) -> str:
    """
    By default, encode into HTML safe string.
    """
    if decode:
        return unescape(data)

    return escape(data)


def md5(data):
    """
    Encrypt string into MD5 hash.
    """
    hashed_value = hashlib.md5(data.encode())
    return hashed_value.hexdigest()



