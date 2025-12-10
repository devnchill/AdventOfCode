def split(arr, a, b, i, j):
    while True:
        if i < 0 or j < 0 or i >= a or j >= b:
            return 0
        if arr[i][j] == "X":
            return 0
        if arr[i][j] == "^":
            arr[i][j] = "X"
            break
        i += 1
    return 1 + split(arr, a, b, i + 1, j - 1) + split(arr, a, b, i + 1, j + 1)


def part1(data):
    arr = [list(a) for a in data.read().strip().split("\n")]
    j = arr[0].index("S")
    a = len(arr)
    b = len(arr[0])
    return split(arr, a, b, 0, j)


def split2(arr, a, b, i, j, cache):
    while True:
        if i < 0 or j < 0 or i >= a or j >= b:
            return 0
        if arr[i][j] == "X":
            return 0
        if (i, j) in cache:
            return cache[(i, j)]
        if arr[i][j] == "^":
            break
        i += 1
    result = (
        1
        + split2(arr, a, b, i + 1, j - 1, cache)
        + split2(arr, a, b, i + 1, j + 1, cache)
    )

    cache[(i, j)] = result
    return result


def part2(data):
    arr = [list(a) for a in data.read().strip().split("\n")]
    j = arr[0].index("S")
    a = len(arr)
    b = len(arr[0])
    cache = {}
    return split2(arr, a, b, 0, j, cache)


with open("input.txt", encoding="utf-8") as file_object:
    print(part1(file_object))
    file_object.seek(0)
    print(part2(file_object) + 1)

