def part1(data):
    lines = [line.split() for line in data.read().strip().split("\n")]
    len_of_row = len(lines[0])

    flat = [item for line in lines for item in line]
    len_of_operands = len(flat) - len_of_row

    arr_of_operands = list(map(int, flat[:len_of_operands]))
    arr_of_operators = flat[len_of_operands:]

    ops = {
        "+": (0, lambda a, b: a + b),
        "-": (0, lambda a, b: a - b),
        "*": (1, lambda a, b: a * b),
        "/": (1, lambda a, b: a / b),
    }

    res = 0
    for start, op in enumerate(arr_of_operators):
        identity, combine = ops[op]
        acc = identity
        for i in range(start, len_of_operands, len_of_row):
            acc = combine(acc, arr_of_operands[i])
        res += acc

    return res


with open("input.txt", encoding="utf-8") as file_object:
    print(part1(file_object))
