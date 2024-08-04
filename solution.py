"""
& is bitwise and
| is bitwise or
x << y is x left shift y places
x >> y is x right shift y places
~ is bitwise not
"""

def signal_and(s1, s2):
    return truncate(s1 & s2)

def signal_or(s1, s2):
    return truncate(s1 | s2)

def signal_lshift(s, n):
    return truncate(s << n)

def signal_rshift(s, n):
    return truncate(s >> n)

def signal_not(s):
    return truncate(~s)

def truncate(value, bit_count=16):
    return value & (2**bit_count - 1)

x = open(0).read().strip().split("\n")
vals = {}

for line in x:
    parts = line.split(" ")
    parts.remove("->")
    if "AND" in parts:
        vals[parts[3]] = signal_and(vals[parts[0]], vals[parts[2]])
    elif "OR" in parts:
        vals[parts[3]] = signal_or(vals[parts[0]], vals[parts[2]])
    elif "LSHIFT" in parts:
        vals[parts[3]] = signal_lshift(vals[parts[0]], int(parts[2]))
    elif "RSHIFT" in parts:
        vals[parts[3]] = signal_rshift(vals[parts[0]], int(parts[2]))
    elif "NOT" in parts:
        vals[parts[2]] = signal_not(vals[parts[1]])
    else:
        vals[parts[1]] = int(parts[0])

print(vals["a"])