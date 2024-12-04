x = open(0).read().splitlines()

t = 0

for i in range(len(x)):
    for j in range(len(x[i])):
        if j <= len(x[i]) - 4:
            if x[i][j:j+4] in ["XMAS", "SAMX"]:
                t += 1
        if i <= len(x) - 4:
            if "".join([x[i+k][j] for k in range(4)]) in ["XMAS", "SAMX"]:
                t += 1
        if j <= len(x[i]) - 4 and i <= len(x) - 4:
            if "".join([x[i+k][j+k] for k in range(4)]) in ["XMAS", "SAMX"]:
                t += 1
        if j >= 3 and i <= len(x) - 4:
            if "".join([x[i+k][j-k] for k in range(4)]) in ["XMAS", "SAMX"]:
                t += 1

print(t)