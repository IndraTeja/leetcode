def roman_integer(s):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = 0
    prev = 0
    for c in s:
        val = roman_dict.get(c)
        if val < prev:
            prev = val
            val = val * (-1)
            integer = integer + val
        else:
            integer = integer + val
            prev = val
    return integer


if __name__ == '__main__':
    s = "IV"
    print(roman_integer(s))
