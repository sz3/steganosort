import json
from os import path
from tempfile import TemporaryDirectory
from unittest import TestCase

from steganosort.cli import enc, dec


SAMPLE_JSON = {
    "1988": 351.57,
    "1989": 353.12,
    "1990": 354.39,
    "1991": 355.61,
    "1992": 356.45,
    "1993": 357.10,
    "1994": 358.83,
    "1995": 360.82,
    "1996": 362.61,
    "1997": 363.73,
    "1998": 366.70,
    "1999": 368.38,
    "2000": 369.55,
    "2001": 371.14,
    "2002": 373.28,
    "2003": 375.80,
    "2004": 377.52,
    "2005": 379.80,
    "2006": 381.90,
    "2007": 383.79,
    "2008": 385.59,
    "2009": 387.43,
    "2010": 389.90,
    "2011": 391.65,
    "2012": 393.86,
    "2013": 396.52,
    "2014": 398.64,
    "2015": 400.83,
    "2016": 404.22,
    "2017": 406.55,
    "2018": 408.52,
    "2019": 411.43,
}


class CliTest(TestCase):
    maxDiff = None

    def setUp(self):
        self.tempdir = TemporaryDirectory()

    def tearDown(self):
        with self.tempdir:
            pass

    def test_encoding(self):
        src_path = path.join(self.tempdir.name, 'infile')
        with open(src_path, 'wt') as fi:
            json.dump(SAMPLE_JSON, fi)

        dst_path = path.join(self.tempdir.name, 'outfile')
        with open(src_path, 'rb') as fi, open(dst_path, 'wt') as fo:
            enc(fi, fo, b'hello!')

        # validate json is the "same"
        with open(dst_path, 'rb') as fo:
            self.assertDictEqual(SAMPLE_JSON, json.load(fo))

        # validate decode
        decode_path = path.join(self.tempdir.name, 'decoded')
        with open(dst_path, 'rb') as fo, open(decode_path, 'wt') as fdec:
            dec(fo, fdec)

        with open(decode_path, 'rb') as fdec:
            self.assertEqual(b'hello!\x00\x00\x00\x00', fdec.read())
