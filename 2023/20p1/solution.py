from copy import deepcopy

z = [[y[0], y[1].split(", ")] for y in [line.split(" -> ") for line in open(0).read().splitlines()]]

for i in range(len(z)):
    if "%" in z[i][0]:
        z[i].append(0)
    elif "&" in z[i][0]:
        z[i].append([])

for i in range(len(z)):
    if "&" in z[i][0]:
        for j in range(len(z)):
            if z[i][0][1:] in z[j][1] and z[j][0] != "broadcaster":
                z[i][2].append([z[j][0][1:], "L"]) 

def flip_flop(y, p):
    if p[0] == "high":
        return None
    
    pulses = []
    if y[2] == 0:
        y[2] = 1
        for i in range(len(y[1])):
            pulses.append(["high", y[1][i], y[0][1:]])
    else:
        y[2] = 0
        for i in range(len(y[1])):
            pulses.append(["low", y[1][i], y[0][1:]])

    return [y, pulses]

def conjunction(y, p):
    send_low = True
    pulses = []
    
    for i in range(len(y[2])):
        if y[2][i][0] == p[2]:
            y[2][i][1] = "H" if p[0] == "high" else "L"
    
    for i in range(len(y[2])):
        if y[2][i][1] == "L":
            send_low = False
            break
    
    if send_low:
        for i in range(len(y[1])):
            pulses.append(["low", y[1][i], y[0][1:]])
    else:
        for i in range(len(y[1])):
            pulses.append(["high", y[1][i], y[0][1:]])
    
    return [y, pulses]

def process_pulse(x, p):
    module_i = None
    for i in range(len(x)):
        if p[1] in x[i][0] and x[i][0] != "broadcaster":
            module_i = i
            break
    
    if module_i == None:
        return None

    if "%" in x[module_i][0]:
        a = flip_flop(x[module_i], p)
        if a:
            x[module_i], pulses = a
        else:
            pulses = None
    elif "&" in x[module_i][0]:
        x[module_i], pulses = conjunction(x[module_i], p)

    if pulses:
        return pulses
    return None   

def press_button(x):
    pulses = [] # pulse is ["low/high", recieving module, sending module]
    nl, nh = 1, 0
    for i in range(len(x)):
        if x[i][0] == "broadcaster":
            y = x[i]

    for i in range(len(y[1])):
        pulses.append(["low", y[1][i], "broadcaster"])

    while pulses:
        new_pulses = []
        for i in range(len(pulses)):
            out = process_pulse(x, pulses[i])
            if pulses[i][0] == "low":
                nl += 1
            else:
                nh += 1
            if out:
                new_pulses.extend(out)
        pulses = new_pulses

    return [x, nl, nh]

def find_pulses(x):
    states = [deepcopy(x)]
    button_presses = 1
    nl, nh = 0, 0
    next_state = press_button(deepcopy(states[-1]))
    nl += next_state[1]
    nh += next_state[2]
    next_state = next_state[0]
    while button_presses < 1000:
        states.append(next_state)
        next_state = press_button(deepcopy(states[-1]))
        button_presses += 1
        nl += next_state[1]
        nh += next_state[2]
        next_state = next_state[0]
    print(nl * nh)

initial = deepcopy(z)

find_pulses(initial)