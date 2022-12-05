from .main import DecoderRing


class DecoderRingInterpreter(DecoderRing):
    def __init__(self):
        super().__init__()

        self._encoder = {
            'base64': self.base64,
            'hex': self.hex,
            'caeser': self.caeser
        }
        self._encryption = {
            "md5": self.encrypt_md5
        }

    def parse(self, options: str):
        """
        Example inputs:

        string --b64 --decode

        string
        --base64 --decode

        string
        --caeser --shift 2
        """
        split = options.split()

        return self._encoder

    def cleanup(self):
        return

    def help(self):
        return
