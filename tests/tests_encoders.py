import unittest

from encoders import Basic, Base64, Hex


class TestBasic(unittest.TestCase):

    def test_wrong_input_type(self):
        test = Basic(data=123)
        self.assertRaises(TypeError, test)


class TestBase64(unittest.TestCase):

    def test_successful_encoding(self):
        """
        Successful Encoding
        """
        test = Base64(data="Encode this").encode()
        self.assertEqual(test,  'RW5jb2RlIHRoaXM=')

    def test_successful_decoding(self):
        """
        Successful Decoding
        """
        test = Base64(data="RW5jb2RlIHRoaXM=").decode()
        self.assertEqual(test,  'Encode this')


if __name__ == '__main__':
    unittest.main()
