f = [y.split() for y in open(0).read().splitlines()]

c = 1
x = 1
i = 0
d = 0
b = 0
t = 0

while c <= 240:
    # setup for cycle
    if d == 0:
        x += b
        if i >= len(f):
            b = 0
        elif f[i][0] == "noop":
            d = 1
            b = 0
        elif f[i][0] == "addx":
            d = 2
            b = int(f[i][1])
        i += 1

    # cycle completes tasks (during)
    if c in [20, 60, 100, 140, 180, 220]:
        t += c*x

    # stuff once cycle ends
    d -= 1
    c += 1

print(t)