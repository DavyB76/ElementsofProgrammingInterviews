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