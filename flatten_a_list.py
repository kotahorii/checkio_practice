def first_word(text: str) -> str:
    text_list = text.split(" ")
    return text_list[0]


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6


def number_length(num: int) -> int:
    return len(str(num))


if __name__ == "__main__":
    print(number_length(10))
