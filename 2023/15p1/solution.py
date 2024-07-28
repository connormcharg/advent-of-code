x = open(0).read().split(",")

boxes = [[] for _ in range(256)]

def hash(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h

total = 0
for step in x:
    total += hash(step)

print(total)