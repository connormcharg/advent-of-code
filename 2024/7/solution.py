from itertools import product as p
from copy import deepcopy

x = [y.split(": ") for y in open(0).read().splitlines()]
t = 0

def check(c, l, v):
    for co in c:
        y = []
        i = 0
        j = 0
        while i < len(l):
            y.append(l[i])
            i += 1
            if len(y) == 2:
                if co[j] == "+":
                    y.append(y.pop() + y.pop())
                elif co[j] == "*":
                    y.append(y.pop() * y.pop())
                else:
                    v1, v2 = y.pop(), y.pop()
                    y.append(int(f"{v2}{v1}"))
                j += 1
        if y[0] == v:
            return True
    return False

for i in range(len(x)):
    x[i][0] = int(x[i][0])
    x[i][1] = [int(y) for y in x[i][1].split(" ")]

    c = list(p(["+", "*", "|"], repeat=len(x[i][1]) - 1))
    if check(c, x[i][1], x[i][0]):
        t += x[i][0]

print(t)

