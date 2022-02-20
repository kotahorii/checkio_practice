import math
from typing import Counter


def isometric_strings(first_word: str, second_word: str) -> bool:
    if first_word == "":
        return second_word == ""
    result_dict: dict[str, str] = {}
    for i in range(len(first_word)):
        if first_word[i] in first_word[:i]:
            if result_dict[first_word[i]] != second_word[i]:
                return False
        else:
            result_dict[first_word[i]] = second_word[i]
    return True


Coords = list[tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    list1 = sorted(
        [
            math.sqrt(
                (coords_1[0][0] - coords_1[1][0]) ** 2
                + (coords_1[0][1] - coords_1[1][1]) ** 2
            ),
            math.sqrt(
                (coords_1[0][0] - coords_1[2][0]) ** 2
                + (coords_1[0][1] - coords_1[2][1]) ** 2
            ),
            math.sqrt(
                (coords_1[1][0] - coords_1[2][0]) ** 2
                + (coords_1[1][1] - coords_1[2][1]) ** 2
            ),
        ]
    )

    list2 = sorted(
        [
            math.sqrt(
                (coords_2[0][0] - coords_2[1][0]) ** 2
                + (coords_2[0][1] - coords_2[1][1]) ** 2
            ),
            math.sqrt(
                (coords_2[0][0] - coords_2[2][0]) ** 2
                + (coords_2[0][1] - coords_2[2][1]) ** 2
            ),
            math.sqrt(
                (coords_2[1][0] - coords_2[2][0]) ** 2
                + (coords_2[1][1] - coords_2[2][1]) ** 2
            ),
        ]
    )
    ratio1 = [list1[0] / list1[1], list1[1] / list1[2], list1[2] / list1[1]]
    ratio2 = [list2[0] / list2[1], list2[1] / list2[2], list2[2] / list2[1]]
    return ratio1 == ratio2


def verify_anagrams(a: str, b: str) -> bool:
    return Counter(a.lower().replace(" ", "")) == Counter(b.lower().replace(" ", ""))


def unix_match(filename: str, pattern: str) -> bool:
    if pattern == "*" or pattern == "**":
        return True
    if "." not in filename:
        return False
    file_no_dot = (
        "".join(filename.split("."))
        if Counter(filename)["."] == 1
        else "".join(filename.split("."))
        + "." * (len("".join(pattern.split("."))) - len("".join(filename.split("."))))
    )
    pattern_no_dot = "".join(pattern.split("."))
    if len(file_no_dot) != len(pattern_no_dot):
        if "*" not in pattern_no_dot:
            return False
        for i in range(len(pattern_no_dot)):
            if file_no_dot[i] != pattern[i]:
                if pattern_no_dot[i] != "?" and pattern_no_dot[i] != "*":
                    return False
        return True
    else:
        for i in range(len(pattern_no_dot)):
            if file_no_dot[i] != pattern_no_dot[i]:
                if pattern_no_dot[i] != "?" and pattern_no_dot[i] != "*":
                    return False
    return True


if __name__ == "__main__":
    print(unix_match("name....", "name.???"))
