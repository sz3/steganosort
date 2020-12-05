import os
from unittest import TestCase

from encodesort.encodesort import encode, decode


class EncodeSortTest(TestCase):
    def test_encode_decode(self):
        carrier = list(range(256))

        data = b'fooooobar'
        res = encode(carrier, data)

        pad = b'\x00' * (128 - len(data))
        self.assertEqual(data + pad, decode(res))

    def test_encode_decode_rng(self):
        carrier = list(range(256))

        for i in range(1000):
            data = os.urandom(128)
            res = encode(carrier, data)
            self.assertEqual(data, decode(res))
