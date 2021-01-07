
from .steganosort import encode as base_encode, decode as base_decode


def _floor_pow_2(x):
    return 2**(x.bit_length() - 1)


def encode(o, bits):
    if isinstance(o, dict):
        return dict_encode(o, bits)
    else:
        return list_encode(o, bits)


def decode(o):
    if isinstance(o, dict):
        return dict_decode(o)
    else:
        return list_decode(o)


def list_encode(l, bits):
    '''
    unlike the base `encode` and `decode`, the `list_??codes` can handle:
        * non-sorted input lists
        * non-power-of-two array sizes
        * duplicate elements
    '''
    viable = set()
    extra = []
    for elem in l:
        if elem not in viable:
            viable.add(elem)
        else:
            extra.append(elem)

    viable = sorted(viable)
    capacity = _floor_pow_2(len(viable))
    extra += viable[capacity:]
    viable = viable[:capacity]

    res = base_encode(viable, bits)
    return res + extra


def list_decode(l):
    '''
    unlike the base `encode` and `decode`, the `smart_??codes` can handle:
        * non-power-of-two array sizes
        * duplicate elements
    '''
    capacity = _floor_pow_2(len(set(l)))
    return base_decode(l[:capacity])


def dict_encode(d, bits):
    d = {k: d[k] for k in sorted(d)}

    indices = list(sorted(d))
    indices = list_encode(list(d.keys()), bits)
    return {k: d[k] for k in indices}


def dict_decode(d):
    return list_decode(list(d.keys()))
