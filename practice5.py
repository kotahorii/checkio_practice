import heapq


def bigger_price(limit: int, data: list):
    def f(n):
        return n[1]

    result: list = []
    for tup in heapq.nlargest(
        limit, [(i, dic["price"]) for i, dic in enumerate(data)], f
    ):
        result.append(data[tup[0]])
    return result


def between_markers(text: str, begin: str, end: str) -> str:
    if begin not in text and end not in text:
        return text
    if begin not in text:
        j = text.index(end)
        return text[:j]
    if end not in text:
        i = text.index(begin) + len(begin)
        return text[i:]

    i = text.index(begin) + len(begin)
    j = text.index(end)
    return text[i:j] if i < j else ""


def popular_words(text: str, words: list[str]) -> dict[str, int]:
    pass


if __name__ == "__main__":
    print(
        popular_words(
            """
When I was One
I had just begun
When I was Two
I was nearly new
""",
            ["i", "was", "three", "near"],
        )
    )
