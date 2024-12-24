inputs, rules = open(0).read().split("\n\n")

inputs = list(map(lambda x: x.split(": "), inputs.splitlines()))
rules = list(map(lambda x: x.split(" "), rules.splitlines()))

wires = {}

for w in inputs:
    wires[w[0]] = int(w[1])

x = ""
y = ""
for i in inputs:
    if i[0][0] == "x":
        x += i[1]
    else:
        y += i[1]

x = x[::-1]
y = y[::-1]
z = bin(int(x, base=2) + int(y, base=2)).replace("0b", "")
z = z[::-1]

for i in range(len(z)):
    wires[f"z{str(i).zfill(2)}"] = int(z[i])

print(wires)