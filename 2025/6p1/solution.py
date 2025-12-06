x = [a.split(" ") for a in open(0).read().strip().splitlines()]

y = []
for i in range(len(x)):
    t = []
    for j in range(len(x[i])):
        if x[i][j] != "":
            t.append(x[i][j])
    y.append(t)

g = 0

for i in range(0, len(y[0])):
    t = 0 if y[-1][i] == "+" else 1
    for j in range(0, len(y) - 1):
        if y[-1][i] == "+":
            t += int(y[j][i])
        else:
            t *= int(y[j][i])
    g += t

print(g)