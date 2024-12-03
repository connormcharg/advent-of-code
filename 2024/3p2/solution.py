import re

x = open(0).read().splitlines()

pattern = r"(mul\((-?\d+),\s*(-?\d+)\)|do\(\)|don't\(\))"

t = 0
do = True

for l in x:
    for y in re.findall(pattern, l):
        if y[0] == "do()":
            do = True
        elif y[0] == "don't()":
            do = False
        else:
            if do:
                t += int(y[1]) * int(y[2])

print(t)