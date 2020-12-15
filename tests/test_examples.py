from json import dumps, loads
from unittest import TestCase

from steganosort.examples import dict_encode, dict_decode


class ExamplesTest(TestCase):
    def test_encode_decode(self):
        baseline = {str(i): i for i in range(32)}
        encoded = dumps(dict_encode(baseline, b'message123'))

        res = dict_decode(loads(encoded))
        self.assertEqual(b'message123', res)
