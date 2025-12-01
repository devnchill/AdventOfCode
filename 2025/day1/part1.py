res = 0
curr = 50
with open("input.txt", encoding="utf-8") as file_object:
    for word in file_object.read().split("\n")[:-1]:
        direction = word[0]
        val = int(word[1:]) % 100
        if direction == "L":
            curr = (curr - val) % 100
        else:
            curr = (curr + val) % 100
        if curr == 0:
            res += 1

    print(res)
