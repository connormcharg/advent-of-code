x = open(0).read().strip().splitlines()

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
t = 0

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
            t += 1

print(t)