from base64 import urlsafe_b64decode, urlsafe_b64encode
from . import utils

"""
Used to quickly encode / decode strings.
"""


class DecoderRing:
    def __init__(self, data: str) -> None:
        self.data: str = data
        self.altered_data: str = ''

        if not isinstance(data, str):
            raise TypeError("Input 'data' requires type 'str'.")

    def __call__(self):
        return {
            "data": self.data,
            "altered_data": self.altered_data
        }

    def _data(self) -> str:
        """
        Use self.altered_data over self.data
        """
        if self.altered_data:
            return self.altered_data
        return self.data

    def base64_encode(self) -> str:
        """
        Encode into Base64 string
        """
        data = self._data()
        encoded = urlsafe_b64encode(data.encode('utf-8'))
        self.altered_data = str(encoded, 'utf-8')
        return self.altered_data

    def base64_decode(self) -> str:
        """
        Decode Base64 string into ASCII
        """
        data = self._data()
        decoded = urlsafe_b64decode(data)
        self.altered_data = decoded.decode()
        return self.altered_data

    def hex_encode(self) -> str:
        """
        Encode into Hexadecimal string
        """
        data = self._data()
        bytes_conversion = data.encode('utf-8')
        self.altered_data = bytes_conversion.hex()
        return self.altered_data

    def hex_decode(self) -> str:
        """
        Decode Hexadecimal into ASCII
        """
        data = self._data()
        self.altered_data = bytes.fromhex(data).decode('utf-8')
        return self.altered_data

    def caeser_encode(self, shift: int = 5) -> str:
        """
        Caeser's Cipher used on a string.
        """
        data = self._data()

        result = ""

        for char in data:
            if tools.is_not_ascii_letter(character=char):  # Account for spaces and special chars.
                result += char
            elif char.isupper():
                enciphered_index = (tools.ascii_to_index(letter=char) + shift) % 26
                result += tools.index_to_ascii(index=enciphered_index, capitalize=True)
            else:
                enciphered_index = (tools.ascii_to_index(letter=char) + shift) % 26
                result += tools.index_to_ascii(index=enciphered_index)
        return result

    def caeser_decode(self, shift: int = 5) -> str:
        """
        Decipher Caeser's Cipher. Shift should be the value that was used to originally encipher the text.
        """
        data = self._data()

        result = ""

        for char in data:
            if tools.is_not_ascii_letter(character=char):  # Account for spaces and special chars.
                result += char
            elif char.isupper():
                enciphered_index = (tools.ascii_to_index(letter=char) - shift) % 26
                result += tools.index_to_ascii(index=enciphered_index, capitalize=True)
            else:
                enciphered_index = (tools.ascii_to_index(letter=char) - shift) % 26
                result += tools.index_to_ascii(index=enciphered_index)
        return result
