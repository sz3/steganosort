import json
import sys

from .util import encode, decode


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


def main(**kwargs):
    msg = kwargs.get('message')
    if not msg:
        pass
    elif msg.startswith('@'):
        with open(msg[1:], 'rb') as f:
            msg = f.read()
    else:
        msg = bytes(msg, 'utf-8')

    mode = 'newlines'
    if kwargs.get('json'):
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
