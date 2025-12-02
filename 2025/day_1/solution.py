def part1(data):
    res, curr = 0, 50
    for word in data:
        direction = word[0]
        val = int(word[1:]) % 100
        if direction == "L":
            curr = (curr - val) % 100
        else:
            curr = (curr + val) % 100
        if curr == 0:
            res += 1

    return res


def part2(data):
    res, curr = 0, 50
    for word in data:
        direction = word[0]
        intial_rotation = int(word[1:])
        total_rotation = intial_rotation // 100
        final_rotation = intial_rotation % 100
        res += total_rotation
        if direction == "L":
            if curr - final_rotation <= 0 and curr != 0:
                res += 1
            curr = (curr - intial_rotation) % 100
        else:
            if curr + final_rotation > 99 and curr != 0:
                res += 1
            curr = (curr + intial_rotation) % 100
    return res


with open("input.txt", encoding="utf-8") as file_object:
    print(part1(file_object))
    file_object.seek(0)
    print(part2(file_object))
