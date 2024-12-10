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

def count_keys_at_depth(d, t, c = 0, f = None):
    if f is None:
        f = set()
    
    if not isinstance(d, dict):
        return 0
    
    if c == t:
        f.update(d.keys())
        return len(d.keys())
    
    for v in d.values():
        if isinstance(v, dict):
            count_keys_at_depth(v, t, c + 1, f)

    return len(f)

find_all(m, 1)

for trailhead in m.values():
    t += count_keys_at_depth(trailhead, 8)

print(t)