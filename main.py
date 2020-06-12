def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


if __name__ == "__main__":
    a_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]
    print(sort_list(a_list))
