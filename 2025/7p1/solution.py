x = [list(a) for a in open(0).read().splitlines()]

beams = []
for i in range(len(x[0])):
    if x[0][i] == "S":
        beams.append((0, i))

t = 0

for i in range(len(x)):
    new_beams = set()
    for b in beams:
        new_b = (b[0] + 1, b[1])
        if new_b[0] >= len(x):
            continue
        if x[new_b[0]][new_b[1]] == "^":
            new_beams.add((new_b[0], new_b[1] + 1))
            new_beams.add((new_b[0], new_b[1] - 1))
            t += 1
        else:
            new_beams.add(new_b)
    beams = list(new_beams)
    
print(t)