x = open(0).read().strip().splitlines()

x = [[a for a in b] for b in x]

def get_removable(x):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    removable = []

    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == ".":
                continue
            c = 0
            for d in dirs:
                pos_to_check = (i + d[0], j + d[1])
                if pos_to_check[0] >= len(x) or pos_to_check[0] < 0 or pos_to_check[1] >= len(x[0]) or pos_to_check[1] < 0:
                    continue
                if x[pos_to_check[0]][pos_to_check[1]] == "@":
                    c += 1
            if c < 4:
                removable.append((i, j))

    return removable

y = get_removable(x)
t = 0

while len(y) > 0:
    t += len(y)
    for i, j in y:
        x[i][j] = "."
    y = get_removable(x)

print(t)