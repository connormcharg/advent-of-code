workflows, parts = [x.split("\n") for x in open(0).read().split("\n\n")]

t = 0

def do_work(workflow, x, m, a, s):
    rules = workflow[workflow.index("{"):][1:-1].split(",")
    for rule in rules:
        if ":" in rule: # rule is a condition
            if ">" in rule:
                if rule[0] == "x" and x > int(rule[2:rule.index(":")]):
                    return rule.split(":")[1]
                elif rule[0] == "m" and m > int(rule[2:rule.index(":")]):
                    return rule.split(":")[1]
                elif rule[0] == "a" and a > int(rule[2:rule.index(":")]):
                    return rule.split(":")[1]
                elif rule[0] == "s" and s > int(rule[2:rule.index(":")]):
                    return rule.split(":")[1]
            elif "<" in rule:
                if rule[0] == "x" and x < int(rule[2:rule.index(":")]):
                    return rule.split(":")[1]
                elif rule[0] == "m" and m < int(rule[2:rule.index(":")]):
                    return rule.split(":")[1]
                elif rule[0] == "a" and a < int(rule[2:rule.index(":")]):
                    return rule.split(":")[1]
                elif rule[0] == "s" and s < int(rule[2:rule.index(":")]):
                    return rule.split(":")[1]
        else:
            return rule
        
def find_wf_index(workflows, wf):
    for i in range(len(workflows)):
        if workflows[i][:workflows[i].index("{")] == wf:
            return i

for part in parts:
    wf = "in"
    part = part[1:-1].split(",")
    x, m, a, s = [int(x[2:]) for x in part]
    while wf != "A" and wf != "R":
        wf = do_work(workflows[find_wf_index(workflows, wf)], x, m, a, s)
    if wf == "A":
        t += x + m + a + s
        continue
    elif wf == "R":
        continue

print(t)