x = open(0).read().split("\n")
blocks = []
temp = []
for line in x:
    if line == "":
        blocks.append(temp)
        temp = []
        continue
    temp.append(line)

def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
            return r
    return 0


t = 0

for block in blocks:
    row = find_mirror(block)
    t += row * 100

    col = find_mirror(list(zip(*block)))
    t += col

print(t)