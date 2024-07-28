x = open(0).read().strip().split("\n")

LB = 7 if len(x) == 5 else 200000000000000
UB = 27 if len(x) == 5 else 400000000000000

hailstones = [(z[0].split(", "), z[1].split(", ")) for z in [y.split(" @ ") for y in x]]

print(x)
print(LB, UB)
print(hailstones)