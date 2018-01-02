map_string_to_numeral = {"0": 0,
                            "1": 1,
                            "2": 2,
                            "3": 3,
                            "4": 4,
                            "5": 5,
                            "6": 6,
                            "7": 7,
                            "8": 8,
                            "9": 9
}

def convertStringToNumeral(input_string):
    result_number = 0
    power_ten = len(input_string) - 1

    for number_char in input_string:
        result_number += map_string_to_numeral[number_char] * pow(10, power_ten)
        power_ten -= 1

    return result_number