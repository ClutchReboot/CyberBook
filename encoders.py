from base64 import urlsafe_b64decode, urlsafe_b64encode

"""
Used to quickly encode / decode strings.
"""


class Basic:
    def __init__(self, data: str) -> None:
        self.data: str = data

        if not isinstance(data, str):
            raise TypeError("Input 'data' requires type 'str'.")


class Base64(Basic):
    def encode(self) -> str:
        encoded = urlsafe_b64encode(self.data.encode('utf-8'))
        return str(encoded, 'utf-8')

    def decode(self) -> str:
        decoded = urlsafe_b64decode(self.data)
        return decoded.decode()


class Hex(Basic):
    def encode(self) -> str:
        bytes_conversion = self.data.encode('utf-8')
        return bytes_conversion.hex()

    def decode(self) -> str:
        return bytes.fromhex(self.data).decode('utf-8')


if __name__ == '__main__':
    print(
        Base64(data="Encode this").encode(),
        sep='\n'
    )
