x = [(y.split()[0], int(y.split()[1])) for y in open(0).read().splitlines()]

seen = set()
h = [0, 0]
t = [0, 0]
dirs = [(0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, 0), (-1, -1), (-1, 1)]

def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

def step():
    global h, t, seen
    if dist(h, t) > 2**0.5:
        for d in dirs:
            if dist(h, (t[0] + d[0], t[1] + d[1])) == 1:
                t[0] += d[0]
                t[1] += d[1]
                seen.add((t[0], t[1]))
                break

                
seen.add((t[0], t[1]))
for s in x:
    if s[0] == "D":
        for i in range(s[1]):
            h[1] -= 1
            step()
    if s[0] == "U":
        for i in range(s[1]):
            h[1] += 1
            step()
    if s[0] == "R":
        for i in range(s[1]):
            h[0] += 1
            step()
    if s[0] == "L":
        for i in range(s[1]):
            h[0] -= 1
            step()

    print(h, t)
    
print(len(seen))