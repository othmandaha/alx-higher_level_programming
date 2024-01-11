#!/usr/bin/python3
def roman_to_int(roman_string):
    main_di = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sub_dict = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4}

    main_list = list(main_di.keys())
    sub_list = list(sub_dict.keys())
    key = ""
    num = 0
    i = 0

    while i < len(roman_string):
        if i + 1 < len(roman_string):
            if roman_string[i] + roman_string[i + 1] in sub_list:
                key = roman_string[i] + roman_string[i + 1]
                num += sub_dict[key]
                i += 2
                continue
        if roman_string[i] in main_list:
            key = roman_string[i]
            num += main_di[key]
            i += 1
        else:
            return None
    return num
