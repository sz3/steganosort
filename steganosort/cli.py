import argparse
import json
import sys
from argparse import RawTextHelpFormatter

from .util import encode, decode


USAGE='''
Examples:
    cat lines.txt | steganosort "message" > encoded.txt
    cat lines.txt | steganosort @msg.txt > encoded.txt
    cat json.txt | steganosort "message" --json > encodedjson.txt
    cat json.txt | steganosort @msg.txt --json > encodedjson.txt
    cat encoded.txt | steganosort > decodedmsg.txt
    cat encodedjson.txt | steganosort > decodedmsg.txt
'''


def enc_json(src, dst, msg):
    data = json.load(src)
    res = encode(data, msg)
    json.dump(res, dst)


def dec_json(src, dst):
    data = json.load(src)
    res = decode(data)
    dst.write(res.decode('utf-8'))


def enc_lines(src, dst, msg):
    lines = [line for line in src]
    for line in encode(lines, msg):
        dst.write(line)


def dec_lines(src, dst):
    lines = [line for line in src]
    res = decode(lines)
    dst.write(res.decode('utf-8'))


def main(args):
    parser = argparse.ArgumentParser('steganosort',
                                     description='Embed messages in the sort order.',
                                     epilog=USAGE,
                                     formatter_class=RawTextHelpFormatter)
    parser.add_argument('message', nargs='?', default=None)
    parser.add_argument('--json',  action='store_true')
    args = parser.parse_args()

    msg = args.message
    if not msg:
        pass
    elif msg.startswith('@'):
        with open(msg[1:], 'rb') as f:
            msg = f.read()
    else:
        msg = bytes(msg, 'utf-8')

    mode = 'newlines'
    if args.json:
        mode = 'json'

    enc = {
        'json': enc_json,
    }.get(mode, enc_lines)

    dec = {
        'json': dec_json,
    }.get(mode, dec_lines)

    if msg:
        enc(sys.stdin, sys.stdout, msg)
    else:
        dec(sys.stdin, sys.stdout)
