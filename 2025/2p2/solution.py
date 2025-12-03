x = open(0).read().split(",")

y = []
for r in x:
    y.append((int(r.split("-")[0]), int(r.split("-")[1])))

def is_invalid(a: str) -> bool:
    for l in range(1, len(a)//2 + 1):
        s = set()
        for i in range(0, len(a), l):
            s.add(a[i:i+l])
        if len(s) == 1:
            return True
    return False

t = 0

for r in y:
    for i in range(r[0], r[1] + 1):
        a = str(i)

        f = is_invalid(a)
        if f:
            t += i

print(t)