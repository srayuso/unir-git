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


if __name__ == "__main__":
    file_path = os.path.join(".", FILENAME)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    print(sort_list(word_list))
