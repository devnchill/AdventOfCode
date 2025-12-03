def part1(data):
    sum = 0
    for bank in data.read().strip().split("\n"):
        max = int(bank[0])
        last = "second_max"
        second_max = -1
        num_to_add = 0
        for i in range(1, len(bank)):
            curr = int(bank[i])
            if curr > max:
                second_max = max
                max = curr
                last = "max"
            elif (curr <= max and curr >= second_max) or (
                max > second_max and last == "max"
            ):
                second_max = curr
                last = "second_max"

        if last == "max":
            num_to_add = second_max * 10 + max
        else:
            num_to_add = max * 10 + second_max
        sum += num_to_add
    return sum


def part1_one_liner(data):
    return sum(
        max(
            int(bank[i] + bank[j])
            for i in range(len(bank))
            for j in range(i + 1, len(bank))
        )
        for bank in data.read().strip().split("\n")
    )


def part2(data):
    sum = 0
    for bank in data.read().strip().split("\n"):
        m = []
        length = len(bank)
        pick_left = 12
        left, right = 0, length - pick_left
        while pick_left > 0:
            right = length - pick_left
            window = bank[left : right + 1]
            max_no = max(window)
            m.append(max_no)
            pick_left -= 1
            left = left + window.index(max_no) + 1
        sum += int("".join(m))
    return sum


with open("input.txt", encoding="utf-8") as file_object:
    print(part1(file_object))
    file_object.seek(0)
    print(part2(file_object))
