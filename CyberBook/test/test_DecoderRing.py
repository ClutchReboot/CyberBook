from CyberBook import DecoderRing
import unittest


class DecoderRingTests(unittest.TestCase):

    def test_successful_hex_encode(self):
        dr = DecoderRing
        self.assertEqual(dr.basic_hex('test'), '74657374')

    def test_successful_hex_decode(self):
        dr = DecoderRing
        self.assertEqual(dr.basic_hex(data='74657374', decode=True), 'test')

    def test_successful_base64_encode(self):
        dr = DecoderRing
        self.assertEqual(dr.base64(data='test'), 'dGVzdA==')

    def test_successful_base64_decode(self):
        dr = DecoderRing
        self.assertEqual(dr.base64(data='dGVzdA==', decode=True), 'test')

    def test_successful_md5_encrypt(self):
        dr = DecoderRing
        self.assertEqual(dr.md5(data='test'), '098f6bcd4621d373cade4e832627b4f6')

    def test_chain_hex_base64_decode(self):
        dr = DecoderRing
        self.assertEqual(dr.basic_hex(
            data=dr.base64(data='NzQ2NTczNzQ=', decode=True), decode=True), 'test')


if __name__ == '__main__':
    unittest.main()
