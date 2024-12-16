import networkx as nx

grid = list(list(map(lambda x: 1 if x == "#" else 0, list(row))) for row in open(0).read().splitlines())
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def build_graph(grid):
    rows, cols = len(grid), len(grid[0])
    G = nx.DiGraph()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                continue

            for d in range(4):
                dr, dc = DIRS[d]
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[r][c] == 0:
                    G.add_edge((r, c, d), (nr, nc, d), weight=1)
                
                G.add_edge((r, c, d), (r, c, (d + 1) % 4), weight=1000)
                G.add_edge((r, c, d), (r, c, (d - 1) % 4), weight=1000)
    
    return G

start = (len(grid) - 2, 1, 1)
goal = (1, len(grid[0]) - 2)

G = build_graph(grid)

goals = [(*goal, d) for d in range(4)]
for g in goals:
    paths = list(nx.all_shortest_paths(G, start, g, weight="weight"))
    tiles = set()
    min_weight = float("inf")
    for p in paths:
        w = nx.path_weight(G, p, weight="weight")
        if w < min_weight:
            min_weight = w
    for p in paths:
        w = nx.path_weight(G, p, weight="weight")
        if w > min_weight:
            continue
        for node in p:
            tiles.add((node[0], node[1]))
    print(len(tiles))
