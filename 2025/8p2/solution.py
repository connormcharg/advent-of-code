x = [tuple([int(b) for b in a.split(",")]) for a in open(0).read().splitlines()]

def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)**0.5

def get_n_closest(x, n):
    closest = []
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if len(closest) >= n:
                d = dist(x[i], x[j])
                if d > closest[-1][0]:
                    continue
                closest.pop(-1)
            d = dist(x[i], x[j])
            a, b = i, j
            closest.append((d, a, b, x[i][0], x[j][0]))
            closest.sort()

    return closest

circuits = []
for i in range(len(x)):
    circuits.append(set([i]))

closest = get_n_closest(x, 10 if len(x) <= 30 else 3919) # I did a manual binary search changing the last number here until len(circuits was 1)

print(closest[-1][-1] * closest[-1][-2])

for i in range(len(closest)):
    a, b = closest[i][1], closest[i][2]
    a_set, b_set = set(), set()
    f = False
    for c in circuits:
        if a in c and b in c:
            f = True
            break
        elif a in c:
            a_set = c
        elif b in c:
            b_set = c
    if f:
        continue
    circuits.remove(a_set)
    circuits.remove(b_set)
    circuits.append(a_set.union(b_set))

print(len(circuits))