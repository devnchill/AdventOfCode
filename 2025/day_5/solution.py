def parse_input(data):
    data = data.read().split("\n\n")
    arr_of_range = data[0].split("\n")
    ids = list(map(int, data[1].strip().split("\n")))
    pair_of_range = []

    for r in arr_of_range:
        k, v = map(int, r.split("-"))
        pair_of_range.append((k, v))

    pair_of_range.sort()
    merged = []
    curr_start, curr_end = pair_of_range[0]
    for s, e in pair_of_range[1:]:
        if s <= curr_end:  # overlap
            curr_end = max(curr_end, e)
        else:
            merged.append((curr_start, curr_end))
            curr_start, curr_end = s, e
    merged.append((curr_start, curr_end))
    ids.sort()
    return merged, ids


def part1(data):
    merged, ids = parse_input(data)
    res = 0
    pointer = 0
    length_of_merged = len(merged)
    for id in ids:
        while int(id) > merged[pointer][1]:
            pointer += 1
            if pointer == length_of_merged:
                return res
        if merged[pointer][0] <= int(id) <= merged[pointer][1]:
            res += 1
    return res


def part2(data):
    merged, _ = parse_input(data)
    res = 0
    for range in merged:
        res += int(range[1]) - int(range[0]) + 1
    return res


with open("input.txt", encoding="utf-8") as file_object:
    print(part2(file_object))
