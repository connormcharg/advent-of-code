x = open(0).read().split("\n\n")

shapes = [a[3:].split("\n") for a in x[:-1]]
grids = [a.split(": ") for a in x[-1].strip().split("\n")]

for i in range(len(shapes)):
    for j in range(len(shapes[i])):
        shapes[i][j] = [(j, k) for k in range(len(shapes[i][j])) if shapes[i][j][k] == "#"]
    shapes[i] = shapes[i][0] + shapes[i][1] + shapes[i][2]
    shapes[i].sort()

for i in range(len(grids)):
    grids[i][0] = [int(a) for a in grids[i][0].split("x")]
    grids[i][1] = [int(a) for a in grids[i][1].split(" ")]

t = 0

for grid in grids:
    dimensions = grid[0]
    shapes_for_grid = grid[1]
    if sum([len(shapes[i])*shapes_for_grid[i] for i in range(len(shapes_for_grid))]) <= dimensions[0] * dimensions[1]:
        t += 1

print(t)
        