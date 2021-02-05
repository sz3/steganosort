[![Build Status](https://github.com/sz3/steganosort/workflows/ci/badge.svg)](https://github.com/sz3/steganosort/actions?query=workflow%3Aci)
[![Coverage Status](https://coveralls.io/repos/github/sz3/steganosort/badge.svg?branch=master)](https://coveralls.io/github/sz3/steganosort?branch=master)

## steganosort

### Sort order steganography

The ordering of an "unordered" list is an information channel.

This library demonstrates how to embed data in the sort order of python (>=3.6) lists, dictionaries, and JSON.

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
> [16, 17, 18, 19, 20, 21, 1, 5, 13, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 14, 32, 33, 2, 34, 35, 36, 0, 37, 38, 39, 4, 40, 12, 41, 8, 42, 43, 7, 44, 45, 46, 47, 48, 15, 49, 50, 51, 3, 52, 54, 55, 56, 58, 59, 60, 57, 61, 53, 11, 62, 63, 10, 9, 6]

> b'hello world!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

## Constraints, and more interesting usage

This approach can only order *unique* elements -- so arrays or lists with duplicate elements gain no additional payload capacity from those duplicate elements.

However, most key:value data types, such as python's `dict`, or the javascript/json `object`, already enforce unique keys. This means you can encode data in the sort order -- for example -- a json object returned over http.

## JSON over HTTP example

There is a very basic http server/client example in the `examples/` subdirectory. The server requires the python `flask` package.

To run the server on port 8000:
```
python -m examples.server
```

A normal HTTP request shows a normal looking HTTP response:
```
curl localhost:8000
```
> {"2004": 377.52, "1995": 360.82, "1997": 363.73, "1998": 366.7, "1991": 355.61, "2005": 379.8, "1996": 362.61, "2006": 381.9, "2008": 385.59, "1988": 351.57, "2009": 387.43, "2010": 389.9, "2011": 391.65, "2012": 393.86, "2015": 400.83, "2014": 398.64, "2013": 396.52, "2016": 404.22, "2001": 371.14, "2017": 406.55, "2018": 408.52, "1989": 353.12, "2003": 375.8, "2007": 383.79, "2019": 411.43, "1990": 354.39, "2002": 373.28, "2000": 369.55, "1992": 356.45, "1999": 368.38, "1994": 358.83, "1993": 357.1}

But if we discard the response body and print the message encoded in the sort order:
```
python -m examples.client
```

> b'M.Loa CO2.'
