x = [line.strip() for line in open(0)]

antennas = []

for i in range(len(x)):
    for j in range(len(x[i])):
        if x[i][j] != ".":
            antennas.append([i, j, x[i][j]])

pairs = []

for i in range(len(antennas)):
    for j in range(i + 1, len(antennas)):
        if antennas[i][2] == antennas[j][2]:
            pairs.append([antennas[i], antennas[j]])

antinodes = set()

for i in range(len(pairs)):
    dr = pairs[i][1][0] - pairs[i][0][0]
    dc = pairs[i][1][1] - pairs[i][0][1]

    a1 = (pairs[i][1][0], pairs[i][1][1])
    a2 = (pairs[i][0][0], pairs[i][0][1])

    while 0 <= a1[0] < len(x) and 0 <= a1[1] < len(x[0]):
        if a1 not in antinodes:
            antinodes.add(a1)

        a1 = (a1[0] + dr, a1[1] + dc)

    while 0 <= a2[0] < len(x) and 0 <= a2[1] < len(x[0]):
        if a2 not in antinodes:
            antinodes.add(a2)

        a2 = (a2[0] - dr, a2[1] - dc)

print(len(antinodes))