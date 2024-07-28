x = open(0).read().split(",")

boxes = [[] for _ in range(256)]

def hash(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h

for s in x:
    box = hash(s[:-1]) if "-" in s else hash(s[:-2])
    if "-" in s:
        i = None
        for lens in boxes[box]:
            if lens[0] == s[:-1]:
                i = lens
                break
        if i is not None:
            boxes[box].remove(lens)
    else:
        i = None
        for lens in boxes[box]:
            if lens[0] == s[:-2]:
                i = boxes[box].index(lens)
                break
        if i is not None:
            boxes[box][i][1] = int(s[-1])
        else:
            boxes[box].append([s[:-2], int(s[-1])])

total = 0
for i in range(256):
    for j in range(len(boxes[i])):
        total += (i+1) * (j+1) * boxes[i][j][1]

print(total)