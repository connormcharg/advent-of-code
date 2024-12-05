x = [y.splitlines() for y in open(0).read().split("\n\n")]

x[0] = list(map(lambda a: [int(b) for b in a.split("|")], x[0]))
x[1] = list(map(lambda a: [int(b) for b in a.split(",")], x[1]))

t = 0

for s in x[1]:
    valid = True
    for r in x[0]:
        if r[0] in s and r[1] in s:
            if s.index(r[0]) > s.index(r[1]):
                valid = False
    if valid:
        t += s[len(s)//2]

print(t)