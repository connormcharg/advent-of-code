import networkx as nx

bytes = [list(map(int, x.split(",")[::-1])) for x in open(0).read().splitlines()]
rows = 6 if len(bytes) < 1000 else 70
cols = rows
no_fallen = 12 if len(bytes) < 1000 else 1024

corrupted = set()
for i in range(no_fallen - 1):
    corrupted.add(tuple(bytes[i]))

while True:
    G = nx.Graph()
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    corrupted.add(tuple(bytes[no_fallen - 1]))

    for r in range(rows + 1):
        for c in range(cols + 1):
            for dr, dc in DIRS:
                if 0 <= r + dr <= rows and 0 <= c + dc <= cols:
                    if (r + dr, c + dc) not in corrupted and (r, c) not in corrupted:
                        G.add_edge((r, c), (r + dr, c + dc))

    p = nx.has_path(G, (0, 0), (rows, cols))
    if not p:
        print(bytes[no_fallen - 1][::-1])
        break
    
    no_fallen += 1