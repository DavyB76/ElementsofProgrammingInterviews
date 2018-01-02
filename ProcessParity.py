def process_parity(input_word):

    parity_result = input_word & 1
    while input_word:
        input_word = input_word >>1

    return parity_result