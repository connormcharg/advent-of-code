x = open(0).read().splitlines()
x = [int(j) for i in x for j in i.split("   ")]

a = [x[i] for i in range(0, len(x), 2)]
b = [x[i] for i in range(1, len(x), 2)]
a.sort()
b.sort()

t = 0
for i in range(len(a)):
    t += abs(a[i] * b.count(a[i]))

print(t)