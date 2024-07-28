x = open(0).read().strip()

r = 0
for i, c in enumerate(x):
    r += 1 if c == "(" else -1
    if r == -1:
        print(i+1)
        exit(0)

print(r)