import re
from collections import Counter
from datetime import date, datetime

# def checkio(array: list[int]) -> int:
#     if not array:
#         return 0
#     result_num = 0
#     for i, num in enumerate(array):
#         if i % 2 == 0:
#             result_num += num
#     return result_num * array[-1]

# best solution
def checkio(array: list[int]) -> int:
    return sum(array[0::2] * array[-1]) if 0 < len(array) else 0


# def is_three_words(text: str) -> bool:
#     str_list = text.split(" ")
#     if len(text) < 3:
#         return False
#     for i, string in enumerate(str_list):
#         if string.isalpha() and i + 2 < len(str_list):
#             if str_list[i + 1].isalpha() and str_list[i + 2].isalpha():
#                 return True
#     return False

# best solution
# def is_three_words(words: str) -> bool:
#     succ = 0
#     for word in words.split():
#         succ = (succ + 1) * word.isalpha()
#         if succ == 3:
#             return True
#         else:
#             return False

# best solution 2
def is_three_words(words):
    return True if re.search("\D+\s\D+\s\D+", words) else False


def left_join(phrases: tuple) -> str:
    return ",".join(phrases).replace("right", "left")


# def first_word(text: str) -> str:
#     # text_list = text.split(".")
#     text_list = re.split("[._ ]", text)
#     for string in text_list:
#         if string == "":
#             continue
#         if string[0].isalpha():
#             return string[:-1] if not string[-1].isalpha() else string
#     return ""

# best solution
# def first_word(text: str) -> str:
#     return re.search("([\w']+)", text).group(1)

# best solution 2
def first_word(text: str) -> str:
    i = 0
    while i < len(text) and text[i] in "., ":
        i += 1
    j = i
    while j < len(text) and text[j] not in "., ":
        j += 1

    return text[i:j]


YearMonthDay = tuple[int, int, int]


# def days_diff(first_tuple: YearMonthDay, second_tuple: YearMonthDay) -> int:
#     diff = datetime(first_tuple[0], first_tuple[1], first_tuple[2]) - datetime(
#         second_tuple[0], second_tuple[1], second_tuple[2]
#     )
#     return abs(diff.days)

# best solution
def days_diff(date1: YearMonthDay, date2: YearMonthDay) -> int:
    f = date(*date1)
    b = date(*date2)
    a = (f - b).days
    return abs(a)


# def count_digits(text: str) -> int:
#     count = 0
#     for k, v in Counter(text).items():
#         if k.isdigit():
#             count += v
#     return count

# best solution
def count_digits(text: str) -> int:
    return sum(map(str.isdigit, text))


def backward_string_by_word(text: str) -> str:
    return " ".join(text.split(" ")[::-1])[::-1]


if __name__ == "__main__":
    print(backward_string_by_word("hello  world"))
    print(list(map(lambda x: x * 2, list(range(5)))))
