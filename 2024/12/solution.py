import networkx as nx

grid = [list(x) for x in open(0).read().splitlines()]
g = nx.Graph()

for i in range(len(grid)):
    for j in range(len(grid[i])):
        f = False
        if i < len(grid) - 1:
            if grid[i][j] == grid[i + 1][j]:
                g.add_edge((i, j), (i + 1, j))
                g.add_edge((i + 1, j), (i, j))
                f = True
        if j < len(grid[i]) - 1:
            if grid[i][j] == grid[i][j + 1]:
                g.add_edge((i, j), (i, j + 1))
                g.add_edge((i, j + 1), (i, j))
                f = True
        if i > 0:
            if grid[i][j] == grid[i - 1][j]:
                g.add_edge((i, j), (i - 1, j))
                g.add_edge((i - 1, j), (i, j))
                f = True
        if j > 0:
            if grid[i][j] == grid[i][j - 1]:
                g.add_edge((i, j), (i, j - 1))
                g.add_edge((i, j - 1), (i, j))
                f = True
        if not f:
            g.add_node((i, j))

c = list(nx.connected_components(g))

def get_sides(r):
    potential_sides = []
    
    for n in r:
        boundaries = []
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (n[0] + d[0], n[1] + d[1]) not in r:
                boundaries.append((n, (n[0] + d[0], n[1] + d[1])))
        for b in boundaries:
            f = False
            fi = -1
            for i in range(len(potential_sides)):
                for s in potential_sides[i]:
                    if (b[1][0] - b[0][0], b[1][1] - b[0][1]) == (s[1][0] - s[0][0], s[1][1] - s[0][1]):
                        if (b[0][1] - b[1][1] != 0 and b[0][1] == s[0][1]) or (b[0][0] - b[1][0] != 0 and b[0][0] == s[0][0]):
                            f = True
                            fi = i
            if f:
                potential_sides[fi].append(b)
            else:
                potential_sides.append([b])

    sides = []
    for p in potential_sides:
        d = (p[0][1][0] - p[0][0][0], p[0][1][1] - p[0][0][1])
        t = []
        for i in range(len(grid)):
            if d[0] == 0:
                if any([x[0] == (i, x[0][1]) for x in p]):
                    t.append(((i, p[0][0][1]), (i, p[0][1][1])))
                else:
                    if t != []:
                        sides.append(t)
                        t = []
            elif d[1] == 0:
                if any([x[0] == (x[0][0], i) for x in p]):
                    t.append(((p[0][0][0], i), (p[0][1][0], i)))
                else:
                    if t != []:
                        sides.append(t)
                        t = []
        if t != []:
            sides.append(t)

    return len(sides)
                        

t = 0
for r in c:
    a = len(r)
    # p = sum(4 - g.degree(n) for n in r)
    p = get_sides(r)
    t += a * p

print(t)
