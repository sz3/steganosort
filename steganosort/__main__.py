import argparse
import sys
from .cli import main

from argparse import RawTextHelpFormatter


USAGE='''
Examples:
    cat lines.txt | steganosort "message" > encoded.txt
    cat lines.txt | steganosort @msg.txt > encoded.txt
    cat json.txt | steganosort "message" --json > encodedjson.txt
    cat json.txt | steganosort @msg.txt --json > encodedjson.txt
    cat encoded.txt | steganosort > decodedmsg.txt
    cat encodedjson.txt | steganosort > decodedmsg.txt
'''


if __name__ == '__main__':
    parser = argparse.ArgumentParser('steganosort',
                                     description='Embed messages in the sort order.',
                                     epilog=USAGE,
                                     formatter_class=RawTextHelpFormatter)
    parser.add_argument('message', nargs='?', default=None)
    parser.add_argument('--json',  action='store_true')
    args = parser.parse_args()
    main(message=args.message, json=args.json)
