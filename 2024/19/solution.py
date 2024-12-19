import re

def foo(s, l):
    r = re.compile("(?:" + "|".join(l) + ")*$")
    if r.match(s) != None:
        return True
    return False

def bar(s, l):
    cache = {}

    def helper(r):
        if r in cache:
            return cache[r]
        
        if not r:
            return 1
        
        c = 0
        for t in l:
            if r.startswith(t):
                c += helper(r[len(t):])
        
        cache[r] = c
        return c
    
    return helper(s)

towels, patterns = open(0).read().split("\n\n")
towels = towels.strip().split(", ")
patterns = patterns.strip().splitlines()

t = 0

for p in patterns:
    if foo(p, towels):
        t += bar(p, towels)

print(t)