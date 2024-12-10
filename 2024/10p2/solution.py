grid = [list(map(int, list(line))) for line in open(0).read().splitlines()]
m = {}
y = 1
t = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            m[(i, j)] = {}

def find_next(m, y):
    global t
    for k in m.keys():
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            r, c = k[0] + dr, k[1] + dc
            if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
                if grid[r][c] == y:
                    if k in m:
                        m[k][(r, c)] = {}
                    else:
                        m[k] = {(r, c): {}}

def find_all(m, d):
    if all([m[k] == {} for k in m.keys()]):
        find_next(m, d)
    for k in m.keys():
        find_all(m[k], d+1)

def count_paths(d, t, c = 0):
    if d == {}:
        return 1 if c == t else 0
    return sum([count_paths(v, t, c + 1) for v in d.values()])

find_all(m, 1)

# import pprint
# pprint.PrettyPrinter(indent=1).pprint(m)

for trailhead in m.values():
    t += count_paths(trailhead, 9)

print(t)