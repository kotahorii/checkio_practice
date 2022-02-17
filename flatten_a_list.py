from collections import Counter


def first_word(text: str) -> str:
    text_list = text.split(" ")
    return text_list[0]


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6


def number_length(num: int) -> int:
    return len(str(num))


def most_frequent(strings: list[str]) -> str:
    count = Counter(strings)
    for k, v in count.items():
        if v >= len(strings) % 2 + len(strings) // 2:
            return k


if __name__ == "__main__":
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))
