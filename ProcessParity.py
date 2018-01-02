def naive_process_parity(input_word):

    parity_result = input_word & 1
    while input_word:
        input_word = input_word >>1

    return parity_result


def lightly_optimized_process_parity(input_number):
    result = 0
    while input_number:
        result ^= 1
        input_number &= input_number - 1
    return result


def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

PRECOMPUTED_PARITY = [parity(i) for i in range(1 << 16)]

def fully_optimized_process_parity(input_number):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED_PARITY[input_number >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(input_number >> (2 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(input_number >> MASK_SIZE) & BIT_MASK] ^
            PRECOMPUTED_PARITY[input_number & BIT_MASK])