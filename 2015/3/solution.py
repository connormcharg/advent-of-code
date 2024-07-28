d = open(0).read().strip()
x1, y1, x2, y2 = 0, 0, 0, 0
r = set()

for i, dir in enumerate(d):
    if i % 2 == 0:
        r.add((x1, y1))
        if dir == "^":
            y1 += 1
        elif dir == ">":
            x1 += 1
        elif dir == "v":
            y1 -= 1
        elif dir == "<":
            x1 -= 1
    else:
        r.add((x2, y2))
        if dir == "^":
            y2 += 1
        elif dir == ">":
            x2 += 1
        elif dir == "v":
            y2 -= 1
        elif dir == "<":
            x2 -= 1

print(len(r))