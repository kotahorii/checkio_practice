from collections import Counter

# def checkio(data: list[int]) -> list[int]:
#     i = 0
#     while i < len(data):
#         if data.count(data[i]) == 1:
#             data.pop(i)
#         else:
#             i += 1

#     return data


# Best solution
def checkio(data):
    count = Counter(data)
    return [n for n in data if count[n] > 1]


if __name__ == "__main__":
    print(checkio([1, 2, 3, 4, 5]))
