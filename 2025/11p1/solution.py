from collections import deque

x = {a.split(": ")[0]: a.split(": ")[1].split(" ") for a in open(0).read().splitlines()}

def bfs_all_paths(adj, start, goal):
    paths = []
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        for nxt in adj.get(node, []):
            if nxt in path:
                continue
            new_path = path + [nxt]
            if nxt == goal:
                paths.append(new_path)
            else:
                queue.append((nxt, new_path))
    return paths

print(len(bfs_all_paths(x, "you", "out")))