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


with open("input.txt", encoding="utf-8") as file_object:
    print(part1(file_object))
    file_object.seek(0)
    # print(part2(file_object))
