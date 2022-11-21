from base64 import urlsafe_b64decode, urlsafe_b64encode

"""
Used to quickly encode / decode strings.
"""


class EncoderDecoder:
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

    def base64_encode(self) -> str:
        if self.altered_data:
            encoded = urlsafe_b64encode(self.altered_data.encode('utf-8'))
        else:
            encoded = urlsafe_b64encode(self.data.encode('utf-8'))
        self.altered_data = str(encoded, 'utf-8')
        return self.altered_data

    def base64_decode(self) -> str:
        if self.altered_data:
            decoded = urlsafe_b64decode(self.altered_data)
        else:
            decoded = urlsafe_b64decode(self.data)
        self.altered_data = decoded.decode()
        return self.altered_data

    def hex_encode(self) -> str:
        if self.altered_data:
            bytes_conversion = self.altered_data.encode('utf-8')
        else:
            bytes_conversion = self.data.encode('utf-8')
        self.altered_data = bytes_conversion.hex()
        return self.altered_data

    def hex_decode(self) -> str:
        if self.altered_data:
            self.altered_data = bytes.fromhex(self.altered_data).decode('utf-8')
        else:
            self.altered_data = bytes.fromhex(self.data).decode('utf-8')
        return self.altered_data
