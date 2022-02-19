import heapq
from collections import Counter
from typing import Optional, Union

# def bigger_price(limit: int, data: list[Union[int, str]]):
#     def f(n: int):
#         return n[1]

#     result: list = []
#     for tup in heapq.nlargest(
#         limit, [(i, dic["price"]) for i, dic in enumerate(data)], f
#     ):
#         result.append(data[tup[0]])
#     return result

# best solution
def bigger_price(
    limit: int, data: list[dict[str, Union[int, str]]]
) -> list[dict[str, Union[int, str]]]:
    data.sort(key=lambda x: x["price"], reverse=True)
    return data[:limit]


# def between_markers(text: str, begin: str, end: str) -> str:
#     if begin not in text and end not in text:
#         return text
#     if begin not in text:
#         j = text.index(end)
#         return text[:j]
#     if end not in text:
#         i = text.index(begin) + len(begin)
#         return text[i:]

#     i = text.index(begin) + len(begin)
#     j = text.index(end)
#     return text[i:j] if i < j else ""

# best solution
def between_markets(text: str, begin: str, end: str) -> str:
    start = text.find(begin) + len(begin) if begin in text else None
    stop = text.find(end) if end in text else None
    return text[start:stop]


def popular_words(text: str, words: list[str]) -> dict[str, int]:
    return {key: Counter(text.lower().split())[key] for key in words}


def second_index(text: str, symbol: str) -> Optional[int]:
    if symbol not in text:
        return

    count = 0
    for i, char in enumerate(text):
        if char == symbol:
            count += 1
        if count == 2:
            return i
    return


def frequency_sort(items: list[int]) -> list[int]:
    return [
        k
        for k, v in sorted(Counter(items).items(), key=lambda x: x[1], reverse=True)
        for _ in range(v)
    ]


if __name__ == "__main__":
    print(frequency_sort([4, 6, 6, 6, 2, 2, 2, 6, 4, 4, 4]))
