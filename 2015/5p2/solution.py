x = open(0).read().strip().split("\n")
t = 0
for line in x:
    f = True
    pairs = []
    for i in range(0, len(line)-1):
        pairs.append(line[i:i+2])
    for i in range(len(pairs)):
        if pairs[i] in pairs[i+2:]:
            f = False
            break
    if f:
        continue
    f = True
    for i in range(0, len(line)-2):
        if line[i] == line[i+2]:
            f = False
            break
    if f:
        continue        
    t += 1
print(t)