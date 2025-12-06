x = [list(a) for a in open(0).read().splitlines()]

t = 0
p = []
s = ""

for i in range(len(x[0]) - 1, -1, -1):
    for j in range(0, len(x)):
        if x[j][i] == " ":
            if j == len(x) - 1:
                if s != "":
                    p.append(int(s))
                    s = ""
        elif x[j][i] in ["+", "*"]:
            p.append(int(s))
            s = ""
            if x[j][i] == "+":
                y = 0
                for z in p:
                    y += z
            else:
                y = 1
                for z in p:
                    y *= z
            t += y
            p = []
        else:
            s += x[j][i]

print(t)