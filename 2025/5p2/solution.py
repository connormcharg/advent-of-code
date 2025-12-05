r, v = [block.splitlines() for block in open(0).read().strip().split("\n\n")]

r = [[int(a.split("-")[0]), int(a.split("-")[1])] for a in r]
v = [int(a) for a in v]

r.sort(key=lambda x: x[0])
f = []
f.append(r[0])

for i in range(1, len(r)):
    l = f[-1]
    c = r[i]

    if c[0] <= l[1]:
        l[1] = max(l[1], c[1])
    else:
        f.append(c)

t = 0

for i in f:
    t += (i[1] - i[0] + 1)

print(t)