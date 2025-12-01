x = [l.strip() for l in open(0).readlines()]
y = []
for l in x:
    y.append((l[0], int(l[1:])))

s = 50
c = 0

for d, a in y:
    if d == "L":
        for b in range(a):
            s -= 1
            if s < 0 or s > 99:
                s = s % 100
            if s == 0:
                c += 1

    elif d == "R":
        for b in range(a):
            s += 1
            if s < 0 or s > 99:
                s = s % 100
            if s == 0:
                c += 1

print(c)