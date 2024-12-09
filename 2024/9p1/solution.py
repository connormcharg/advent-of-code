x = open(0).read().strip()
y = True
z = []
w = 0

for c in x:
    if y:
        z.extend([str(w) for _ in range(int(c))])
        w += 1
    else:
        z.extend(["." for _ in range(int(c))])
    y = not y

def check_done(l):
    for i in range(l.index("."), len(l)):
        if l[i] != ".":
            return False
    return True

def get_last(l):
    for i in range(len(l) - 1, -1, -1):
        if l[i] != ".":
            return i
    return -1

def get_first_empty(l):
    for i in range(len(l)):
        if l[i] == ".":
            return i
    return -1

while not check_done(z):
    a = get_first_empty(z)
    b = get_last(z)
    z[a] = z[b]
    z[b] = "."

print(sum([int(z[i]) * i for i in range(len(z)) if z[i] != "."]))