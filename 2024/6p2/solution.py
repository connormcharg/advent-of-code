from copy import deepcopy

grid = [[int(y) for y in x.replace(".", "0").replace("#", "1").replace("^", "2")] for x in open(0).read().splitlines()]
rotate = lambda d: (d[1], -d[0])

def check(grid, block):
    p, d = (-1, -1), (-1, 0)
    seen = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                p = (i, j)
                grid[i][j] = 0
    seen.add((p, d))

    c = 0

    while -1 < p[0] < len(grid) and -1 < p[1] < len(grid[0]) and c < 10000:
        new_p = (p[0] + d[0], p[1] + d[1])
        if not (-1 < new_p[0] < len(grid) and -1 < new_p[1] < len(grid[0])):
            return False
        if grid[new_p[0]][new_p[1]] != 1 and (new_p[0], new_p[1]) != block:
            p = new_p
        else:
            d = rotate(d)
        if (p, d) in seen:
            return True
        seen.add((p, d))
        c += 1
    return True

t = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if check(deepcopy(grid), (i, j)):
            t += 1
    print(i)

print(t)
