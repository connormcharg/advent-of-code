inputs, rules = open(0).read().split("\n\n")

inputs = list(map(lambda x: x.split(": "), inputs.splitlines()))
rules = list(map(lambda x: x.split(" "), rules.splitlines()))

wires = {}

for w in inputs:
    wires[w[0]] = int(w[1])

while rules != []:
    t = []
    for r in rules:
        if r[0] in wires and r[2] in wires:
            match r[1]:
                case "AND":
                    wires[r[4]] = int(bool(wires[r[0]]) and bool(wires[r[2]]))
                case "OR":
                    wires[r[4]] = int(bool(wires[r[0]]) or bool(wires[r[2]]))
                case "XOR":
                    wires[r[4]] = int(bool(wires[r[0]]) ^ bool(wires[r[2]]))  
        else:
            t.append(r)
            continue
    rules = t

wires = dict(sorted(wires.items()))
# for k, v in wires.items():
#     print(k, v)

b = ""
for v in [wires[k] for k in wires.keys() if k[0] == "z"]:
    b += str(v)
b = b[::-1]

print(int(b, base=2))