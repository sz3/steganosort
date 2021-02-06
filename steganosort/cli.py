import json
import sys

from .util import encode, decode


USAGE='''
steganosort - Embed messages in the sort order of JSON arrays and objects.

Usage:
    cat json.txt | steganosort "message" > encoded.txt
    cat json.txt | steganosort @msg.txt > encoded.txt
    cat encoded.txt | steganosort > decodedmsg.txt
'''


def enc(src, dst, msg):
    data = json.load(src)
    res = encode(data, msg)
    json.dump(res, dst)


def dec(src, dst):
    data = json.load(src)
    res = decode(data)
    dst.write(res.decode('utf-8'))


def main(args):
    msg = ''
    if len(args) > 1:
        arg = args[1]
        if arg in ['-h', '--help']:
            print(USAGE)
            return
        if arg.startswith('@'):
            with open(arg[1:], 'rb') as f:
                msg = f.read()
        else:
            msg = bytes(arg, 'utf-8')
    if msg:
        enc(sys.stdin, sys.stdout, msg)
    else:
        dec(sys.stdin, sys.stdout)
