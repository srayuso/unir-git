"""
License: MIT
Organization: UNIR
"""

import os

FILENAME = "words.txt"


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


def to_uppercase(items):
    return [word.upper() for word in items if word is not None]


if __name__ == "__main__":
    file_path = os.path.join(".", FILENAME)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    print(to_uppercase(sort_list(word_list)))
