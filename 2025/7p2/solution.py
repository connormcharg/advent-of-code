x = [list(a) for a in open(0).read().splitlines()]

beams = []
for i in range(len(x[0])):
    if x[0][i] == "S":
        beams.append((0, i))

grid = [[0 for i in range(len(x[0]))] for j in range(len(x))]
grid[beams[0][0]][beams[0][1]] = 1

for i in range(len(x)):
    new_beams = []
    for b in beams:
        new_b = (b[0] + 1, b[1])
        if new_b[0] >= len(x):
            continue
        if x[new_b[0]][new_b[1]] == "^":
            new_beams.append((new_b[0], new_b[1] + 1))
            new_beams.append((new_b[0], new_b[1] - 1))
            grid[new_b[0]][new_b[1] + 1] += grid[b[0]][b[1]]
            grid[new_b[0]][new_b[1] - 1] += grid[b[0]][b[1]]
        else:
            new_beams.append(new_b)
            grid[new_b[0]][new_b[1]] += grid[b[0]][b[1]]
    beams = list(set(new_beams))

print(sum(grid[-1]))