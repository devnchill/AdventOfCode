from itertools import zip_longest
import math


def part1(data):
    lines = [line.split() for line in data.read().strip().split("\n")]
    len_of_row = len(lines[0])

    flat = [item for line in lines for item in line]
    len_of_operands = len(flat) - len_of_row

    arr_of_operands = list(map(int, flat[:len_of_operands]))
    arr_of_operators = flat[len_of_operands:]

    ops = {
        "+": (0, lambda a, b: a + b),
        "*": (1, lambda a, b: a * b),
    }

    res = 0
    for start, op in enumerate(arr_of_operators):
        identity, combine = ops[op]
        acc = identity
        for i in range(start, len_of_operands, len_of_row):
            acc = combine(acc, arr_of_operands[i])
        res += acc

    return res


def part2(data):
    lines = [line for line in data.read().strip().split("\n")]
    columns = list(zip_longest(*lines, fillvalue=" "))
    answer = 0
    ops = {
        "+": lambda arr: sum(arr),
        "*": lambda arr: math.prod(arr),
    }
    arr_of_cols_for_same_operator = []
    for i in range(len(columns) - 1, -1, -1):
        is_operator = columns[i][-1] in "+*"
        is_space = len([e for e in columns[i] if e.isdigit()]) == 0 and not is_operator
        if is_space:
            continue
        arr_of_cols_for_same_operator.append(
            int("".join(a for a in columns[i] if a.isdigit()))
        )
        if is_operator:
            operator = columns[i][-1]
            print(f"operator for index {i} is {operator}")
            answer += ops[operator](arr_of_cols_for_same_operator)
            arr_of_cols_for_same_operator = []
    return answer


with open("input.txt", encoding="utf-8") as file_object:
    # print(part1(file_object))
    # file_object.seek(0)
    print(part2(file_object))
