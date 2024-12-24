import networkx as nx

track = [list(x) for x in open(0).read().strip().splitlines()]
rows = len(track)
cols = len(track[0])

s, e = None, None

for r in range(rows):
    for c in range(cols):
        if track[r][c] == "S":
            s = (r, c)
            track[r][c] = "."
        elif track[r][c] == "E":
            e = (r, c)
            track[r][c] = "."

G = nx.DiGraph()

for r in range(1, rows - 1):
    for c in range(1, cols - 1):
        if track[r][c] != "#":
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if track[r + dr][c + dc] != "#":
                    G.add_edge((r, c), (r + dr, c + dc))

ORIGINAL_TIME = nx.dijkstra_path_length(G, s, e)

t = 0

for r in range(1, rows - 1):
    for c in range(1, cols - 1):
        if track[r][c] != "#":
            for dr, dc in [(-2, 0), (0, 2), (2, 0), (0, -2)]:
                if 0 <= r + dr < rows and 0 <= c + dc < cols:
                    if track[r + dr][c + dc] != "#":
                        G.add_edge((r, c), (r + dr, c + dc))
                        new_time = nx.dijkstra_path_length(G, s, e)
                        # print(new_time)
                        if ORIGINAL_TIME - new_time >= 100:
                            t += 1
                        G.remove_edge((r, c), (r + dr, c + dc))

print(t)