import json
import sys

from .util import encode, decode


def enc(src, dst, msg):
    data = json.load(src)
    res = encode(data, msg)
    json.dump(res, dst)


def dec(src, dst):
    data = json.load(src)
    res = decode(data)
    dst.write(res.decode('utf-8'))


def main():
    msg = ''
    if len(sys.argv) > 1:
        msg = bytes(sys.argv[1], 'utf-8')
    if msg:
        enc(sys.stdin, sys.stdout, msg)
    else:
        dec(sys.stdin, sys.stdout)
