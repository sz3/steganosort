
from .steganosort import encode as base_encode, decode as base_decode


def _floor_pow_2(x):
    return 2**(x.bit_length() - 1)


def encode(o, bits, sort_fun=None):
    if isinstance(o, dict):
        return dict_encode(o, bits, sort_fun)
    else:
        return list_encode(o, bits, sort_fun)


def decode(o, sort_fun=None):
    if isinstance(o, dict):
        return dict_decode(o, sort_fun)
    else:
        return list_decode(o, sort_fun)


def list_encode(l, bits, sort_fun=None):
    '''
    unlike the base `encode` and `decode`, the `list_??codes` can handle:
        * non-sorted input lists
        * non-power-of-two array sizes
        * duplicate elements
    '''
    sort_fun = sort_fun or sorted
    viable = set()
    extra = []
    for elem in l:
        if elem not in viable:
            viable.add(elem)
        else:
            extra.append(elem)

    viable = sort_fun(viable)
    capacity = _floor_pow_2(len(viable))
    extra += viable[capacity:]
    viable = viable[:capacity]

    res = base_encode(viable, bits)
    return res + extra


def list_decode(l, sort_fun=None):
    '''
    unlike the base `encode` and `decode`, the `smart_??codes` can handle:
        * non-power-of-two array sizes
        * duplicate elements
    '''
    capacity = _floor_pow_2(len(set(l)))
    return base_decode(l[:capacity], sort_fun)


def dict_encode(d, bits, sort_fun=None):
    sort_fun = sort_fun or sorted
    d = {k: d[k] for k in sort_fun(d)}

    indices = list(d.keys())
    indices = list_encode(indices, bits)
    return {k: d[k] for k in indices}


def dict_decode(d, sort_fun=None):
    return list_decode(list(d.keys()), sort_fun)
