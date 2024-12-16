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

def find_lowest_score_path(grid, start, goal):
    G = build_graph(grid)

    start_state = (*start, 1)
    goal_states = [(goal[0], goal[1], d) for d in range(4)]

    lengths, paths = nx.single_source_dijkstra(G, start_state)

    min_cost, best_path = float("inf"), None
    for goal_state in goal_states:
        if goal_state in lengths and lengths[goal_state] < min_cost:
            min_cost = lengths[goal_state]
            best_path = paths[goal_state]
    
    return min_cost, best_path

start = (len(grid) - 2, 1)
goal = (1, len(grid[0]) - 2)

min_cost, best_path = find_lowest_score_path(grid, start, goal)
print(min_cost)