from base64 import urlsafe_b64decode, urlsafe_b64encode
import hashlib

from . import utils


class DecoderRing:
    """
    Many options for encoding / decoding.
    Also includes some encryption options such as MD5.
    """
    def __init__(self, data: str = '') -> None:
        self.data: str = data
        self.altered_data: str = ''

        self.shift: int = 0

        if not isinstance(data, str):
            raise TypeError("Input 'data' requires type 'str'.")

    def __call__(self):
        return {
            "data": self.data,
            "altered_data": self.altered_data
        }

    def _assign_data(self) -> str:
        """
        Use self.altered_data over self.data
        """
        if self.altered_data:
            return self.altered_data
        return self.data

    def set_data(self, data: str):
        """
        Setter function. To be used with interpreter.
        """
        self.data = data
        return self.data

    def base64(self, decode: bool = False) -> str:
        """
        By default, encode into Base64 string.
        """

        data = self._assign_data()

        if decode:
            decoded = urlsafe_b64decode(data)
            self.altered_data = decoded.decode()
            return self.altered_data

        encoded = urlsafe_b64encode(data.encode('utf-8'))
        self.altered_data = str(encoded, 'utf-8')
        return self.altered_data

    def hex(self, decode: bool = False) -> str:
        """
        By default, encode into Hexadecimal string
        """
        data = self._assign_data()

        if decode:
            self.altered_data = bytes.fromhex(data).decode('utf-8')
            return self.altered_data

        bytes_conversion = data.encode('utf-8')
        self.altered_data = bytes_conversion.hex()
        return self.altered_data

    def caeser(self, shift: int = 5, decode: bool = False) -> str:
        """
        Caeser's Cipher used on a string.
        """
        data = self._assign_data()

        if self.shift:
            shift = self.shift

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
        self.altered_data = result
        return self.altered_data

    def md5(self):
        """
        Encrypt string into MD5 hash.
        """
        data = self._assign_data()
        hashed_value = hashlib.md5(data.encode())
        self.altered_data = hashed_value.hexdigest()
        return self.altered_data
