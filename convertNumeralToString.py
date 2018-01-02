map_numeral_to_string = {0: "0",
                            1: "1",
                            2: "2",
                            3: "3",
                            4: "4",
                            5: "5",
                            6: "6",
                            7: "7",
                            8: "8",
                            9: "9"
}


def convertNumeralToString(input_number):
    result_string = ""

    while input_number > 9:
        modulo_10 = input_number % 10
        result_string = map_numeral_to_string[modulo_10] + result_string
        input_number = (input_number - modulo_10) / 10

    result_string = map_numeral_to_string[input_number] + result_string

    return result_string