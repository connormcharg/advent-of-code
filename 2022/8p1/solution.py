x = open(0).read().splitlines()

t = 2*len(x) + 2*(len(x[0]) - 2)

for i in range(1, len(x) - 1):
    for j in range(1, len(x[i]) - 1):
        y = int(x[i][j])
        down = [int(x[a][j]) < y for a in range(i+1, len(x))]
        up = [int(x[a][j]) < y for a in range(i-1, -1, -1)]
        right = [int(x[i][a]) < y for a in range(j+1, len(x[i]))]
        left = [int(x[i][a]) < y for a in range(j-1, -1, -1)]
        if down != [] and all(down):
            t += 1
        elif up != [] and all(up):
            t += 1
        elif right != [] and all(right):
            t += 1
        elif left != [] and all(left):
            t += 1

print(t)