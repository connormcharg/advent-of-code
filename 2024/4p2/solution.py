x = open(0).read().splitlines()

t = 0

for i in range(1, len(x) - 1):
    for j in range(1, len(x[i]) - 1):
        if x[i][j] == "A":
            if (x[i-1][j-1], x[i+1][j+1]) in [("M", "S"), ("S", "M")]:
                if (x[i-1][j+1], x[i+1][j-1]) in [("M", "S"), ("S", "M")]:
                    t += 1

print(t)