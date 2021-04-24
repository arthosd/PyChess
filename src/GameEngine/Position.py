"""
Script qu traite la position
"""

pattern_number_string = {
    7: "1",
    6: "2",
    5: "3",
    4: "4",
    3: "5",
    2: "6",
    1: "7",
    0: "8",
}

pattern_letter_string = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}


pattern_letter = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
}

pattern_number = {
    "8": 0,
    "7": 1,
    "6": 2,
    "5": 3,
    "4": 4,
    "3": 5,
    "2": 6,
    "1": 7,
}


def tulpe_position(letter, number):
    return (pattern_letter[letter], pattern_number[number])


def string_position(position):
    return pattern_letter_string[position[0]]+pattern_number_string[position[1]]
