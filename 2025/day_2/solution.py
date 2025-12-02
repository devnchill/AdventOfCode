def part1(data):
    sum = 0
    for r in (x.strip() for x in data.read().strip().split(",")):
        lower_range, higher_range = r.split("-")
        for num in range(int(lower_range), int(higher_range) + 1):
            str_num = str(num)
            length = len(str_num)
            if length % 2 != 0:
                continue
            if str_num[0 : length // 2] in str_num[length // 2 :]:
                sum += num

    return sum


def part2(data):
    sum = 0
    for r in (x.strip() for x in data.read().strip().split(",")):
        lower_range, higher_range = r.split("-")
        for num in range(int(lower_range), int(higher_range) + 1):
            str_num = str(num)
            length = len(str_num)
            if length == 1:
                continue

            for i in range(1, (length // 2) + 1):
                if length % i != 0:
                    continue
                curr_substr = str_num[0:i]
                if length == (str_num.count(curr_substr) * i):
                    print(num, "in even handler")
                    sum += num
                    break

    return sum


with open("input.txt", encoding="utf-8") as file_object:
    print(part1(file_object))
    file_object.seek(0)
    print(part2(file_object))
