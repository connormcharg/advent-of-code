from itertools import combinations

x = [list(map(int, x.split(" "))) for x in open(0).read().splitlines()]

def check(s):
    if s[1] > s[0]:
        ascending = True
    else:
        ascending = False
    failed = False
    gap = -1
    for i in range(1, len(s)):
        if ascending and s[i] < s[i-1]:
            failed = True
            break
        if not ascending and s[i] > s[i-1]:
            failed = True
            break
        if abs(s[i] - s[i-1]) < 1 or abs(s[i] - s[i-1]) > 3:
            failed = True
            break
    return not failed

t = 0

for s in x:
    if check(s) or any([check(t) for t in list(combinations(s, len(s)-1))]):
        t += 1

print(t)