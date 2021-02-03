[![Build Status](https://github.com/sz3/steganosort/workflows/ci/badge.svg)](https://github.com/sz3/steganosort/actions?query=workflow%3Aci)
[![Coverage Status](https://coveralls.io/repos/github/sz3/steganosort/badge.svg?branch=master)](https://coveralls.io/github/sz3/steganosort?branch=master)

## steganosort

Hide information in the sort order of a python list or dictionary.

Based on https://github.com/CalderWhite/gif-msg.

## Installation

Use `pip`:
```
pip install steganosort
```

or from source,
```
python setup.py build
python setup.py install
```

## Usage

```
from steganosort import encode, decode
x = list(range(64))
y = encode(x, b'hello world!')
y
decode(y)
```

Expected output:
```
[16, 17, 18, 19, 20, 21, 1, 5, 13, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 14, 32, 33, 2, 34, 35, 36, 0, 37, 38, 39, 4, 40, 12, 41, 8, 42, 43, 7, 44, 45, 46, 47, 48, 15, 49, 50, 51, 3, 52, 54, 55, 56, 58, 59, 60, 57, 61, 53, 11, 62, 63, 10, 9, 6]
b'hello world!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
```

## Constraints, and more interesting usage

This approach can only order *unique* elements -- so arrays or lists with duplicate elements gain no additionally payload capacity from those duplicate elements.

However, most key:value data types, such as python's `dict`, or the javascript/json `object`, already enforce unique keys. This means you can encode data in the sort order -- for example -- a json object returned over http.

There is a very basic http server/client example in the `examples/` subdirectory. The server requires the python `flask` package.

To run the server on port 8000:
```
python -m examples.server
```

To make an http request against the server, discard the response body, and print the message encoded in the sort order:
```
python -m examples.client
```

Expected client output:
```
b'M.Loa CO2.'
```
