r, v = [block.splitlines() for block in open(0).read().strip().split("\n\n")]

r = [(int(a.split("-")[0]), int(a.split("-")[1])) for a in r]
v = [int(a) for a in v]

t = 0

for i in v:
    f = False
    for j in r:
        if j[0] <= i <= j[1]:
            f = True
            break
    if f:
        t += 1

print(t)