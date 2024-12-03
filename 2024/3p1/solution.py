import re

x = open(0).read().splitlines()

pattern = r"mul\((-?\d+),\s*(-?\d+)\)"

t = 0

for l in x:
    for y in re.findall(pattern, l):
        t += int(y[0]) * int(y[1])

print(t)