grid, moves = open(0).read().split("\n\n")

grid = [list(row) for row in grid.splitlines()]
moves = "".join(moves.splitlines())

wide_grid = []
for r in range(len(grid)):
    t = []
    for c in range(len(grid[r])):
        tile = grid[r][c]
        if tile == "#":
            t.extend(["#", "#"])
        elif tile == "O":
            t.extend(["[", "]"])
        elif tile == ".":
            t.extend([".", "."])
        elif tile == "@":
            t.extend(["@", "."])
    wide_grid.append(t)

grid = wide_grid

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

def can_pos_move_in_dir(r, c, d):
    dr, dc = d
    nr, nc = r + dr, c + dc
    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
        if grid[nr][nc] == ".":
            return True
        elif grid[nr][nc] == "#":
            return False
        elif dr == 0:
            lc = -1
            for i in range(c + dc, -1 if dc == -1 else len(grid[0]), dc):
                if grid[r][i] == ".":
                    lc = i
                    break
                if grid[r][i] == "#":
                    break
            if lc != -1:
                return True
        else:
            if grid[nr][nc] == "[":
                return can_pos_move_in_dir(nr, nc, d) and can_pos_move_in_dir(nr, nc + 1, d)
            elif grid[nr][nc] == "]":
                return can_pos_move_in_dir(nr, nc, d) and can_pos_move_in_dir(nr, nc - 1, d)

def move_in_dir(r, c, d):
    dr, dc = d
    nr, nc = r + dr, c + dc
    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
        if dr == 0:
            lc = -1
            stack = []
            for i in range(c + dc, -1 if dc == -1 else len(grid[0]), dc):
                if grid[r][i] == ".":
                    lc = i
                    stack.append((r, i, grid[r][i - dc]))
                    break
                if grid[r][i] == "#":
                    break
                stack.append((r, i, grid[r][i - dc]))
            if lc != -1:
                while len(stack) > 0:
                    n = stack.pop()
                    grid[n[0]][n[1]] = n[2]
                grid[r][c] = "."
                return
        else:
            if grid[nr][nc] == ".":
                grid[nr][nc] = grid[r][c]
                grid[r][c] = "."
            elif grid[nr][nc] == "]":
                move_in_dir(nr, nc, d)
                move_in_dir(nr, nc - 1, d)
                grid[nr][nc] = grid[r][c]
                grid[r][c] = "."
            elif grid[nr][nc] == "[":
                move_in_dir(nr, nc, d)
                move_in_dir(nr, nc + 1, d)
                grid[nr][nc] = grid[r][c]
                grid[r][c] = "."

for m in moves:
    d = dirs[m]
    if can_pos_move_in_dir(rr, rc, d):
        move_in_dir(rr, rc, d)
        rr += d[0]
        rc += d[1]
    # for row in grid:
    #     print(row)
    # print("----------------")

t = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "[":
            t += 100 * i + j

print(t)