parts = [x.splitlines() for x in open(0).read().split("\n\n")]
locks = []
keys = []

for p in parts:
    if p[0] == ".....":
        keys.append(p)
    else:
        locks.append(p)

def replace_with_heights(parts):
    for i in range(len(parts)):
        new = []
        for c in range(len(parts[i][0])):
            new.append(sum([1 for r in range(len(parts[i])) if parts[i][r][c] == "#"]) - 1)
        parts[i] = new

replace_with_heights(locks)
replace_with_heights(keys)

t = 0

for l in locks:
    for k in keys:
        if all([l[i] + k[i] <= 5 for i in range(len(l))]):
            t += 1

print(t)