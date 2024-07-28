from itertools import combinations
from turtle import pos

x = open(0).read().strip().split("\n")

LB = 7 if len(x) == 5 else 200000000000000
UB = 27 if len(x) == 5 else 400000000000000

hailstones = [[[int(w) for w in z[0].split(", ")], [int(w) for w in z[1].split(", ")]] for z in [y.split(" @ ") for y in x]]
combos = list(combinations(range(len(hailstones)), 2))

total = 0

for c in combos:
    p1x, p1y, _ = hailstones[c[0]][0]
    p2x, p2y, _ = hailstones[c[1]][0]
    v1x, v1y, _ = hailstones[c[0]][1]
    v2x, v2y, _ = hailstones[c[1]][1]
    m1 = v1y / v1x
    m2 = v2y / v2x
    if m1 == m2:
        continue
    possible_x = (p2y - p1y + m1*p1x - m2*p2x) / (m1 - m2)
    possible_y = p1y + m1*(possible_x - p1x)
    # if in test area
    in_area = False
    if LB <= possible_x <= UB and LB <= possible_y <= UB:
        in_area = True
    else:
        continue
    # if in future for 1 and 2
    future = [False, False]
    if (possible_x > p1x and v1x > 0) or (possible_x < p1x and v1x < 0):
        if (possible_y > p1y and v1y > 0) or (possible_y < p1y and v1y < 0):
            future[0] = True
        else:
            continue
    else:
        continue
    if (possible_x > p2x and v2x > 0) or (possible_x < p2x and v2x < 0):
        if (possible_y > p2y and v2y > 0) or (possible_y < p2y and v2y < 0):
            future[1] = True
        else:
            continue
    else:
        continue
    if in_area and all(future):
        total += 1

print(total)