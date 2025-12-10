from collections import deque

def to_mask(bits):
    m = 0
    for i, b in enumerate(bits):
        if b:
            m |= 1 << i
    return m

def min_presses_bfs(target_mask, op_masks, bitlen):
    start = 0
    if start == target_mask:
        return 0

    visited = [False] * (1 << bitlen)
    visited[start] = True

    q = deque([(start, 0)])

    while q:
        state, dist = q.popleft()

        for op in op_masks:
            nxt = state ^ op
            if not visited[nxt]:
                if nxt == target_mask:
                    return dist + 1
                visited[nxt] = True
                q.append((nxt, dist + 1))

    return None

x = [a.split(" ") for a in open(0).read().splitlines()]

machines = []
for a in x:
    t = []
    for b in a:
        if b[0] == "[":
            u = []
            for c in b[1:-1]:
                u.append(0 if c == "." else 1)
            t.append(u)
        elif b[0] == "(":
            t.append([int(c) for c in b.strip("()").split(",")])
        elif b[0] == "{":
            t.append([int(c) for c in b.strip("{}").split(",")])
    machines.append(t)

t = 0

for machine in machines:
    target_bits = machine[0]
    toggle_sets = machine[1:-1]

    bitlen = len(target_bits)
    target_mask = to_mask(target_bits)

    op_masks = []
    for toggle in toggle_sets:
        m = 0
        for i in toggle:
            m ^= 1 << i
        op_masks.append(m)

    c = min_presses_bfs(target_mask, op_masks, bitlen)
    
    t += c

print(t)
