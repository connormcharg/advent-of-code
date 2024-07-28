points = [(0, 0)]
dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

hex_to_dir = {"0": "R", "1": "D", "2": "L", "3": "U"}

b = 0

for line in open(0):
    x = line.split()[2][1:-1]
    d = hex_to_dir[x[-1]]
    n = int(x[1:-1], 16)
    dr, dc = dirs[d]
    b += n
    r, c = points[-1]
    points.append((r + dr * n, c + dc * n))

A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
i = A - b // 2 + 1

print(i + b)