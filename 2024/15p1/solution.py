grid, moves = open(0).read().split("\n\n")

grid = [list(row) for row in grid.splitlines()]
moves = "".join(moves.splitlines())

rr, rc = -1, -1

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "@":
            rr, rc = i, j

dirs = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

for move in moves:
    dr, dc = dirs[move]
    if grid[rr + dr][rc + dc] == ".":
        grid[rr + dr][rc + dc] = "@"
        grid[rr][rc] = "."
        rr += dr
        rc += dc
        continue
    elif grid[rr + dr][rc + dc] == "#":
        continue
    lr, lc = -1, -1
    if dr != 0:
        for i in range(rr + dr, -1 if dr == -1 else len(grid), dr):
            if grid[i][rc] == ".":
                lr = i
                lc = rc
                break
            if grid[i][rc] == "#":
                break
    elif dc != 0:
        for i in range(rc + dc, -1 if dc == -1 else len(grid[0]), dc):
            if grid[rr][i] == ".":
                lr = rr
                lc = i
                break
            if grid[rr][i] == "#":
                break
    if lr != -1 and lc != -1:
        grid[lr][lc] = "O"
        grid[rr + dr][rc + dc] = "@"
        grid[rr][rc] = "."
        rr += dr
        rc += dc
    
t = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "O":
            t += 100 * i + j

print(t)