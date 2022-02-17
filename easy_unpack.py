def easy_unpack(elements: tuple) -> tuple[int, int, int]:
    return (elements[0], elements[2], elements[-2])


def remove_all_before(items: list, border: int) -> list[int]:
    return items


if __name__ == "__main__":
    print(remove_all_before([1, 2, 3, 4, 5], 3))
