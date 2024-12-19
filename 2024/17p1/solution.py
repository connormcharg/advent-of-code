import math
from copy import deepcopy

registers, program = open(0).read().split("\n\n")

a, b, c = [int(line.split(": ")[1]) for line in registers.splitlines()]
program_original = list(map(int, program.split(" ")[1].strip().split(",")))
i = 0
o = ""
program = deepcopy(program_original)

def combo(v):
    global a, b, c
    if v == 4:
        v = a
    elif v == 5:
        v = b
    elif v == 6:
        v = c
    return v

def adv(v):
    global a, i
    v = combo(v)
    numerator = a
    denominator = 2 ** v
    a = math.floor(numerator / denominator)
    i += 2

def bxl(v):
    global b, i
    b = b ^ v
    i += 2

def bst(v):
    global b, i
    v = combo(v)
    b = v % 8
    i += 2

def jnz(v):
    global a, i
    if a == 0:
        i += 2
        return
    i = v

def bxc(v):
    global b, c, i
    b = b ^ c
    i += 2

def out(v):
    global o, i
    v = combo(v)
    v = v % 8
    if o == "":
        o += str(v)
        i += 2
        return
    o += f",{v}"
    i += 2

def bdv(v):
    global a, b, i
    v = combo(v)
    numerator = a
    denominator = 2 ** v
    b = math.floor(numerator / denominator)
    i += 2

def cdv(v):
    global a, c, i
    v = combo(v)
    numerator = a
    denominator = 2 ** v
    c = math.floor(numerator / denominator)
    i += 2

opcodes = {
    0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv
}

def check_eq(p, o):
    s = ""
    for n in p:
        if s == "":
            s = str(n)
        else:
            s += "," + str(n)
    return s == o

def run(r1, r2, r3, p):
    global program, a, b, c, i, o
    program = p
    i = 0
    a, b, c = r1, r2, r3
    o = ""

    while 0 <= i <= len(program) - 2:
        opcodes[program[i]](program[i + 1])

    print(o)

run(a, b, c, program_original)
