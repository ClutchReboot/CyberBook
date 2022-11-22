import unittest

from EncoderDecoderRing import EDR


class TestBasic(unittest.TestCase):

    def test_wrong_input_type(self):
        test = EDR(data=123)
        self.assertRaises(TypeError("Input 'data' requires type 'str'."), test)


class TestBase64(unittest.TestCase):

    def test_successful_encoding(self):
        """
        Successful Encoding
        """
        test = EDR(data="Encode this").base64_encode()
        self.assertEqual(test,  'RW5jb2RlIHRoaXM=')

    def test_successful_decoding(self):
        """
        Successful Decoding
        """
        test = EDR(data="RW5jb2RlIHRoaXM=").base64_decode()
        self.assertEqual(test,  'Encode this')


if __name__ == '__main__':
    unittest.main()
