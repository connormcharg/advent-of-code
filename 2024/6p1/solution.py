x = [[z for z in y] for y in open(0).read().splitlines()]

dirs = {
    "^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1] 
}
# row, col
pos = [-1, -1]
direction = "^"
seen = set()

for l in x:
    for c in l:
        if c in ["^", ">", "v", "<"]:
            pos = [x.index(l), l.index(c)]
            x[x.index(l)][l.index(c)] = "."

seen.add(tuple(pos))

while 0 <= pos[0] < len(x) and 0 <= pos[1] < len(x[0]):
    d = dirs[direction]
    new_pos = [pos[0] + d[0], pos[1] + d[1]]
    if not (0 <= new_pos[0] < len(x) and 0 <= new_pos[1] < len(x[0])):
        break
    if x[new_pos[0]][new_pos[1]] != ".":
        if direction == "^":
            direction = ">"
        elif direction == ">":
            direction = "v"
        elif direction == "v":
            direction = "<"
        elif direction == "<":
            direction = "^"
    else:
        pos = new_pos
        seen.add(tuple(pos))

print(len(seen))