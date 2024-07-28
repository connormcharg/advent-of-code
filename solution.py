from itertools import combinations

x = [y.replace(": ", " ").split(" ") for y in open(0).read().strip().split("\n")]
y = {}

for s in x:
    for i in range(len(s)):
        if i == 0: # add all others
            if s[i] in y:
                y[s[i]].extend([s[j] for j in range(len(s)) if j != i and s[j] not in y[s[i]]])
            else:
                y[s[i]] = [s[j] for j in range(len(s)) if j != i]
        else: # only add first one
            if s[i] in y:
                y[s[i]].append(s[0])
            else:
                y[s[i]] = [s[0]]

print(y)