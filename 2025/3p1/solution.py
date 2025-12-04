x = open(0).read().strip().splitlines()

t = 0

for l in x:
    max = -1
    for i in range(0, len(l) - 1):
        if max != -1:
            if int(l[i]) < int(str(max)[0]):
                continue
        for j in range(i + 1, len(l)):
            c = int(l[i] + l[j])
            if c > max:
                max = c
    t += max

print(t)