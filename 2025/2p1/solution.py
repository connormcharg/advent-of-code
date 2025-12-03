x = open(0).read().split(",")

y = []
for r in x:
    y.append((int(r.split("-")[0]), int(r.split("-")[1])))

t = 0

for r in y:
    for i in range(r[0], r[1] + 1):
        a = str(i)
        if len(a) % 2 == 0:
            if a[:len(a)//2] == a[len(a)//2:]:
                t += i

print(t)