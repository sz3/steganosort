import os
from unittest import TestCase

from steganosort.steganosort import encode, decode


def _pad(data, length):
    pad = b'\x00' * (length - len(data))
    return data + pad


class SteganosortTest(TestCase):
    def test_encode_decode(self):
        carrier = list(range(256))

        data = b'fooooobar'
        res = encode(carrier, data)
        res = decode(res)

        self.assertEqual(128, len(res))
        self.assertEqual(_pad(data, len(res)), res)

    def test_encode_decode_rng(self):
        carrier = list(range(256))

        for i in range(1000):
            data = os.urandom(128)
            res = encode(carrier, data)
            self.assertEqual(data, decode(res))

    def test_encode_decode_5_bits(self):
        carrier = list(range(32))

        data = b'fooooobar'
        res = encode(carrier, data)
        res = decode(res)

        self.assertEqual(10, len(res))
        self.assertEqual(_pad(data, len(res)), res)

    def test_encode_decode_3_bits(self):
        # this is the smallest size, and only encodes ~12 bits.
        # the lower bits of the second byte will not make the trip
        carrier = list(range(8))

        trials = {
            b'ao': b'a`',
            b'oO': b'o@',
        }
        for i, o in trials.items():
            res = encode(carrier, i)
            res = decode(res)
            self.assertEqual(o, res)

    def test_encode_decode_various_bit_lengths(self):
        bits = {
            16: 4,
            32: 10,
            64: 24,
            128: 56,
            256: 128,
            512: 288,
            1024: 640,
            2048: 1408,
            4096: 3072,
        }
        for envelope_size, payload_size in bits.items():
            carrier = list(range(envelope_size))

            data = os.urandom(payload_size)
            res = encode(carrier, data)
            res = decode(res)

            self.assertEqual(payload_size, len(res))
            self.assertEqual(_pad(data, payload_size), res)
