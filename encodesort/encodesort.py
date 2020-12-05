

def encode(carrier, bits):
    cap = len(carrier)
    assert(cap == 256)  # eventually: power of 2?

    desired_bitlen = cap // 2
    assert(len(bits) <= desired_bitlen)
    padded_bits = bits + (b'\0' * (desired_bitlen - len(bits)))
    idx = []

    bigguns = []
    for i, b in enumerate(padded_bits):
        to_encode = int(b)
        big = min(cap - i - 1, to_encode)
        bigguns.append(big)

        # the inserts are relative, to achieve the effect of a series of contiguous, sparse arrays laid atop one another
        # the order of the inserts is small (low array size) to large
        small = to_encode - big
        idx.insert(small, carrier[cap - i - 1])

    for i in range(len(padded_bits)-1, -1, -1):
        idx.insert(bigguns[i], carrier[i])
    return idx


def decode(encoded):
    carrier = sorted(encoded)

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

    return bytes(decoded)


def main():
    carrier = list(range(256))
    bits = b'heliowarbd'
    es = encode(carrier, bits)
    print(es)


if __name__ == '__main__':
    main()
