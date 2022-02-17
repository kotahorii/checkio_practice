def easy_unpack(elements: tuple) -> tuple[int, int, int]:
    len_tuple = len(elements)
    return (elements[0], elements[2], elements[len_tuple - 2])


if __name__ == "__main__":
    print(easy_unpack((6, 2, 9, 4, 3, 9)))
