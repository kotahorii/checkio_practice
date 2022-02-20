from collections import Counter
from operator import itemgetter


def checkio(number: int) -> int:
    result = 1
    count = Counter(str(number))
    for k, v in count.items():
        if int(k) != 0:
            result *= int(k) ** v
    return result


def is_acceptable_password(text: str) -> bool:
    count = 0
    if len(text) < 6:
        return False
    if "password" in text.lower():
        return False
    if len(Counter(text)) < 3:
        return False

    if len(text) <= 9:
        for char in text:
            if char.isdigit():
                count += 1
        return count != len(text) and count >= 1
    else:
        return True


def is_all_upper(text: str) -> bool:
    return text.isupper()


def is_ascending(numbers: list[int]) -> bool:
    len_numbers = len(numbers)
    for i in range(len_numbers - 1):
        if numbers[i] >= numbers[i + 1]:
            return False
    return True


def sort_by_ext(files: list[str]) -> list[str]:
    split_list = sorted([s.split(".") for s in files], key=itemgetter(0))
    print(split_list)
    i = 0
    j = i + 1
    while i < len(split_list) - 1:
        if split_list[i][0] != "" or len(split_list[i]) > 2:
            while j < len(split_list):
                if len(split_list[j]) > 2 and split_list[j][2] == "":
                    split_list[i], split_list[j] = split_list[j], split_list[i]
                    j += 1
                    continue

                if len(split_list[i]) > len(split_list[j]):
                    split_list[i], split_list[j] = split_list[j], split_list[i]
                else:
                    if split_list[i][1] > split_list[j][1]:
                        if len(split_list[i]) >= len(split_list[j]):
                            split_list[i], split_list[j] = split_list[j], split_list[i]
                        else:
                            j += 1
                            continue
                j += 1
        i += 1
        j = i + 1
    return [".".join(s) for s in split_list]


if __name__ == "__main__":
    print(
        sort_by_ext(
            [
                ".config",
                "my.doc",
                "1.exe",
                "345.bin",
                "green.bat",
                "format.c",
                "no.name.",
                "best.test.exe",
            ]
        )
    )
