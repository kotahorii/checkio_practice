def checkio(data: list) -> list[int]:
    map: dict[int, int] = {}
    results = []
    for num in data:
        if num not in map:
            map[num] = 1
        else:
            map[num] += 1
    for k, v in map.items():
        print(k, v)
        if v >= 2:
            for _ in range(v):
                results.append(k)
    return results


if __name__ == "__main__":
    print(checkio([1, 2, 3, 1, 3]))
