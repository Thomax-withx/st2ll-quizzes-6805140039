def convert(number: str) -> int:
    roman_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    if not isinstance(number, str) or not number.strip():
        raise ValueError("Input must be a non-empty string")

    number = number.upper().strip()

    # Check that the Roman numeral follows the correct format
    valid_roman = (
        r"^M{0,3}(CM|CD|D?C{0,3})"
        r"(XC|XL|L?X{0,3})"
        r"(IX|IV|V?I{0,3})$"
    )

    import re

    if not re.match(valid_roman, number):
        raise ValueError(f"'{number}' is not a valid Roman numeral")

    total = 0

    for i in range(len(number)):
        current_value = roman_map[number[i]]

        if i + 1 < len(number) and current_value < roman_map[number[i + 1]]:
            total -= current_value
        else:
            total += current_value

    return total
