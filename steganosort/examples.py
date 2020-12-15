
from .steganosort import encode, decode


def dict_encode(d, bits):
    d = {k: d[k] for k in sorted(d)}

    indices = list(sorted(d))
    indices = encode(indices, bits)
    return {k: d[k] for k in indices}


def dict_decode(d):
    return decode(list(d.keys()))
