import math


class PayloadTooLargeException(Exception):
    def __init__(self, bits, cap):
        super().__init__(f"{len(bits)} is larger than capacity {cap}")


def _get_power_of_2(n):
    return math.log2(n)


def iterate_bits(bits, sz):
    if sz == 8:
        yield from bits
    else:
        from bitstring import BitStream, ReadError
        bs = BitStream(bits)
        while True:
            try:
                yield bs.read(f'uint:{sz}')
            except ReadError:
                break


def _to_bytes(decoded, sz):
    if sz == 8:
        return bytes(decoded)
    else:
        from bitstring import BitStream, Bits
        bs = BitStream()
        for val in decoded:
            bs.append(Bits(uint=int(val), length=sz))
        return bs.tobytes()


def capacity(array_size):
    halfway = array_size // 2
    bit_size = int(math.log2(array_size))
    return (halfway * bit_size) // 8


def encode(carrier, bits):
    if isinstance(bits, str):
       bits = bits.encode('utf-8')

    array_size = len(carrier)
    bit_size = math.log2(array_size)
    assert(bit_size.is_integer())
    halfway = array_size // 2

    cap = capacity(array_size)
    if array_size == 8:  # special case for 8 -- doesn't divide into a byte
        cap = 2
    if len(bits) > cap:
        raise PayloadTooLargeException(bits, cap)

    padded_bits = bits + (b'\0' * (cap - len(bits)))

    idx = []
    bigguns = []
    for i, b in enumerate(iterate_bits(padded_bits, int(bit_size))):
        if i >= halfway:
            break
        to_encode = int(b)
        big = min(array_size - i - 1, to_encode)
        bigguns.append(big)

        # the inserts are relative, to achieve the effect of a series of contiguous, sparse arrays laid atop one another
        # the order of the inserts is small (low array size) to large, letting the later inserts reassign the earliers'
        # indices
        small = to_encode - big
        idx.insert(small, carrier[array_size - i - 1])

    for i in range(halfway-1, -1, -1):
        idx.insert(bigguns[i], carrier[i])

    return idx


def decode(encoded, sort_fun=None):
    sort_fun = sort_fun or sorted
    carrier = sort_fun(encoded)
    bit_size = int(math.log2(len(encoded)))

    decoded_count = len(carrier) // 2
    decoded = [0] * decoded_count

    for i in range(decoded_count):
        index = encoded.index(carrier[i])
        encoded.pop(index)
        decoded[i] = index

    for i in range(decoded_count, len(carrier)):
        index = encoded.index(carrier[i])
        encoded.pop(index)
        decoded[decoded_count - i - 1] += index

    return _to_bytes(decoded, bit_size)

