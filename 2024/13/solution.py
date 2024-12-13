import sympy as sym

x = [y.strip().split("\n") for y in open(0).read().split("\n\n")]

t = 0
for m in x:
    a = list(map(int, list(map(lambda y: y[2:], m[0].split(": ")[1].split(", ")))))
    b = list(map(int, list(map(lambda y: y[2:], m[1].split(": ")[1].split(", ")))))
    p = list(map(int, list(map(lambda y: y[2:], m[2].split(": ")[1].split(", ")))))
    i, j = sym.symbols("i,j")
    eq1 = sym.Eq(a[0]*i + b[0]*j, p[0] + 10000000000000)
    eq2 = sym.Eq(a[1]*i + b[1]*j, p[1] + 10000000000000)
    result = sym.solve([eq1, eq2], (i, j))
    if int(result[i]) == result[i] and int(result[j]) == result[j]:
        t += 3 * result[i] + result[j]

print(t)