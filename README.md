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
y = encode(x, b'helloworld')
decode(y)
```
