def part1(grid):
    grid = grid.read().strip().split("\n")
    no_of_rows = len(grid)
    no_of_cols = len(grid[0])
    accessible_rol = 0
    index = [
        [0, 1],
        [0, -1],
        [-1, 0],
        [+1, 0],
        [-1, -1],
        [+1, -1],
        [-1, +1],
        [+1, +1],
    ]
    for i in range(no_of_rows):
        for j in range(no_of_cols):
            if grid[i][j] == "@":
                roll = 0
                for a, b in index:
                    c, d = a + i, b + j
                    if (
                        c >= 0
                        and d >= 0
                        and c < no_of_rows
                        and d < no_of_cols
                        and grid[c][d] == "@"
                    ):
                        roll += 1
                if roll < 4:
                    accessible_rol += 1
    return accessible_rol


def part2(grid):
    grid = grid.read().strip().split("\n")
    grid = [list(row) for row in grid]
    no_of_rows = len(grid)
    no_of_cols = len(grid[0])
    index = [
        [0, 1],
        [0, -1],
        [-1, 0],
        [+1, 0],
        [-1, -1],
        [+1, -1],
        [-1, +1],
        [+1, +1],
    ]
    accessible_rol = 0
    while True:
        current_accessible_roll = 0
        for i in range(no_of_rows):
            for j in range(no_of_cols):
                print(grid[i][j])
                if grid[i][j] == "@":
                    roll = 0
                    for a, b in index:
                        c, d = a + i, b + j
                        if (
                            c >= 0
                            and d >= 0
                            and c < no_of_rows
                            and d < no_of_cols
                            and grid[c][d] == "@"
                        ):
                            roll += 1
                    if roll < 4:
                        current_accessible_roll += 1
                        grid[i][j] = "X"
        accessible_rol += current_accessible_roll
        if current_accessible_roll == 0:
            break
    return accessible_rol


with open("input.txt", encoding="utf-8", mode="r+") as file_object:
    print(part1(file_object))
    file_object.seek(0)
    print(part2(file_object))
