import math


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


def encode(carrier, bits):
    cap = len(carrier)
    bit_size = math.log2(cap)
    assert(bit_size.is_integer())
    desired_bitlen = cap // 2  # this isn't right, I think
    assert(len(bits) <= desired_bitlen)

    padded_bits = bits + (b'\0' * (desired_bitlen - len(bits)))

    idx = []
    bigguns = []
    for i, b in enumerate(iterate_bits(padded_bits, int(bit_size))):
        if i >= desired_bitlen:
            break
        to_encode = int(b)
        big = min(cap - i - 1, to_encode)
        bigguns.append(big)

        # the inserts are relative, to achieve the effect of a series of contiguous, sparse arrays laid atop one another
        # the order of the inserts is small (low array size) to large
        small = to_encode - big
        idx.insert(small, carrier[cap - i - 1])

    for i in range(desired_bitlen-1, -1, -1):
        idx.insert(bigguns[i], carrier[i])

    return idx


def decode(encoded):
    carrier = sorted(encoded)
    bit_size = int(math.log2(len(encoded)))

    decoded_count = len(encoded) // 2
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


def main():
    carrier = list(range(256))
    bits = b'heliowarbd'
    es = encode(carrier, bits)
    print(es)


if __name__ == '__main__':
    main()
