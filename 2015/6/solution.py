x = [a.split(" ") for a in open(0).read().strip().split("\n")]
y = []
for line in x:
    if line[0] == "toggle":
        y.append(["toggle", tuple(int(z) for z in line[1].split(",")), tuple(int(z) for z in line[3].split(","))])
    elif line[0] == "turn" and line[1] == "on":
        y.append(["on", tuple(int(z) for z in line[2].split(",")), tuple(int(z) for z in line[4].split(","))])
    else:
        y.append(["off", tuple(int(z) for z in line[2].split(",")), tuple(int(z) for z in line[4].split(","))])

lights = [[0 for i in range(1000)] for i in range(1000)]

for line in y:
    if line[0] == "toggle":
        for i in range(line[1][0], line[2][0]+1):
            for j in range(line[1][1], line[2][1]+1):
                lights[i][j] += 2
    elif line[0] == "on":
        for i in range(line[1][0], line[2][0]+1):
            for j in range(line[1][1], line[2][1]+1):
                lights[i][j] += 1
    elif line[0] == "off":
        for i in range(line[1][0], line[2][0]+1):
            for j in range(line[1][1], line[2][1]+1):
                lights[i][j] = max(0, lights[i][j]-1)

print(sum([sum(lights[i]) for i in range(1000)]))