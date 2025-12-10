x = [[int(b) for b in a.split(",")] for a in open(0).read().splitlines()]

m = 0

for a in x:
    for b in x:
        area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        m = max(area, m)

print(m)