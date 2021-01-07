from json import dumps, loads
from unittest import TestCase

from steganosort.util import dict_encode, dict_decode, list_encode, list_decode


class UtilTest(TestCase):
    def test_encode_decode_list(self):
        baseline = list(range(32))
        encoded = dumps(list_encode(baseline, b'message123'))

        res = list_decode(loads(encoded))
        self.assertEqual(b'message123', res)

    def test_encode_decode_list_padded(self):
        baseline = list(range(40))
        encoded = list_encode(baseline, b'message123')
        self.assertEqual(len(baseline), len(encoded))

        res = list_decode(encoded)
        self.assertEqual(b'message123', res)

    def test_encode_decode_dict(self):
        baseline = {str(i): i for i in range(32)}
        encoded = dumps(dict_encode(baseline, b'message123'))

        res = dict_decode(loads(encoded))
        self.assertEqual(b'message123', res)

    def test_encode_decode_dict_padded(self):
        baseline = {str(i): i for i in range(45)}
        encoded = dict_encode(baseline, b'message123')
        self.assertEqual(len(baseline), len(encoded))

        res = dict_decode(encoded)
        self.assertEqual(b'message123', res)
