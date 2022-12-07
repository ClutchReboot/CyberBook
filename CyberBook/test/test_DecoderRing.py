from CyberBook import DecoderRing
import unittest


class DecoderRingTests(unittest.TestCase):

    def test_invalid_data_input(self):
        with self.assertRaises(TypeError):
            DecoderRing(data=74657374)

    def test_successful_hex_encode(self):
        dr = DecoderRing(data='test')
        self.assertEqual(dr.hex(), '74657374')

    def test_successful_hex_decode(self):
        dr = DecoderRing(data='74657374')
        self.assertEqual(dr.hex(decode=True), 'test')

    def test_successful_base64_encode(self):
        dr = DecoderRing(data='test')
        self.assertEqual(dr.base64(), 'dGVzdA==')

    def test_successful_base64_decode(self):
        dr = DecoderRing(data='dGVzdA==')
        self.assertEqual(dr.base64(decode=True), 'test')

    def test_successful_md5_encrypt(self):
        dr = DecoderRing(data='test')
        self.assertEqual(dr.md5(), '098f6bcd4621d373cade4e832627b4f6')

    def test_chain_hex_base64_md5(self):
        dr = DecoderRing(data='test')
        dr.hex()
        dr.base64()
        self.assertEqual(dr.md5(), 'd3808ae5169407ecee946a6d3173b965')

    def test_chain_hex_base64_decode(self):
        dr = DecoderRing(data='NzQ2NTczNzQ=')
        dr.base64(decode=True)
        self.assertEqual(dr.hex(decode=True), 'test')


if __name__ == '__main__':
    unittest.main()
