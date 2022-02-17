def first_word(text: str) -> str:
    text_list = text.split(" ")
    return text_list[0]


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6


def number_length(num: int) -> int:
    return len(str(num))


# def most_frequent(strings: list[str]) -> str:
#     count = Counter(strings)
#     for k, v in count.items():
#         if v >= len(strings) % 2 + len(strings) // 2:
#             return k

# best solution
def most_frequent(data: list[str]) -> str:
    return max(set(data), key=data.count)


# def end_zeros(num: int) -> int:
#     num_list = [int(i) for i in str(num)]
#     i = len(num_list) - 1
#     count = 0
#     while i >= 0:
#         if num_list[i] == 0:
#             count += 1
#         else:
#             break
#         i -= 1
#     return count

# best solution
def end_zeros(num: int) -> int:
    return len(s := str(num)) - len(s.strip("0"))


def backward_string(val: str):
    val_list = [s for s in val]
    len_str = len(val)
    index = 0
    while index < (len_str - 1) / 2:
        val_list[index], val_list[len_str - 1 - index] = (
            val_list[len_str - 1 - index],
            val_list[index],
        )
        index += 1
    return "".join(val_list)


if __name__ == "__main__":
    print(backward_string("hello"))
