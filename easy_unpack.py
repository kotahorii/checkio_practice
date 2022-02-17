# best solution
def easy_unpack(elements: tuple) -> tuple[int, int, int]:
    return (elements[0], elements[2], elements[-2])


# def remove_all_before(items: list, border: int) -> list[int]:
#     index = 0
#     if items is None:
#         return []
#     if border not in items:
#         return items
#     index = items.index(border)
#     return items[index:]

# best solution
def remove_all_before(items: list[int], border: int) -> list[int]:
    return items[items.index(border) :] if border in items else items


def is_all_upper(strings: str) -> bool:
    return strings.upper() == strings


def replace_first(items: list[int]) -> list[int]:
    return items[1:] + items[:1]


def max_digit(number: int) -> int:
    return max([int(i) for i in str(number)])


# def split_pairs(chars: str) -> list[str]:
#     len_chars = len(chars)
#     result_list: list[str] = []
#     for i in range(0, len_chars, 2):
#         if i + 1 > len_chars - 1:
#             result_list.append(chars[i] + "_")
#         else:
#             result_list.append(chars[i] + chars[i + 1])
#     return result_list

# best solution
def split_pairs(a: str) -> list[str]:
    a += "_" if len(a) % 2 else ""
    return [a[i : i + 2] for i in range(0, len(a), 2)]


# def beginning_zeros(number: str) -> int:
#     count = 0
#     len_number = len(number)
#     while count < len_number:
#         if number[count] != "0":
#             break
#         count += 1
#     return count

# best solution
def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip("0"))


def nearest_value(values: set[int], one: int) -> int:
    nearest_value = min({abs(value - one) for value in values})
    return one - nearest_value if one - nearest_value in values else one + nearest_value


def between_markers(text: str, begin: str, end: str) -> str:
    text = text.split(begin)[-1].split(end)[0]
    return text


if __name__ == "__main__":
    print(between_markers("[an apple]", "[", "]"))
