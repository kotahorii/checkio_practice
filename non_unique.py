def checkio(data: list[int]) -> list[int]:
    i = 0
    while i < len(data):
        if data.count(data[i]) == 1:
            data.pop(i)
        else:
            i += 1

    return data


if __name__ == "__main__":
    print(checkio([1, 2, 3, 4, 5]))
