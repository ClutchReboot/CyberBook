from base64 import urlsafe_b64decode, urlsafe_b64encode
import hashlib

from . import utils


class DecoderRing:
    """
    Many options for encoding / decoding.
    Also includes some encryption options such as MD5.
    """
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
            if utils.is_not_ascii_letter(character=char):  # Account for spaces and special chars.
                result += char
            elif char.isupper():
                enciphered_index = (utils.ascii_to_index(letter=char) + shift) % 26
                result += utils.index_to_ascii(index=enciphered_index, capitalize=True)
            else:
                enciphered_index = (utils.ascii_to_index(letter=char) + shift) % 26
                result += utils.index_to_ascii(index=enciphered_index)
        return result

    def caeser_decode(self, shift: int = 5) -> str:
        """
        Decipher Caeser's Cipher. Shift should be the value that was used to originally encipher the text.
        """
        data = self._data()

        result = ""

        for char in data:
            if utils.is_not_ascii_letter(character=char):  # Account for spaces and special chars.
                result += char
            elif char.isupper():
                enciphered_index = (utils.ascii_to_index(letter=char) - shift) % 26
                result += utils.index_to_ascii(index=enciphered_index, capitalize=True)
            else:
                enciphered_index = (utils.ascii_to_index(letter=char) - shift) % 26
                result += utils.index_to_ascii(index=enciphered_index)
        return result

    def encrypt_md5(self):
        data = self._data()
        hashed_value = hashlib.md5(data.encode())
        return hashed_value.hexdigest()
