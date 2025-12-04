x = open(0).read().strip().splitlines()

def find_largest(b, n):
    start = 0
    end = len(b) - n

    if start == end:
        return b

    max = -1
    max_i = -1
    for i in range(start, end + 1):
        if int(b[i]) > max:
            max = int(b[i])
            max_i = i

    if n == 1:
        return str(max)

    return str(max) + find_largest(b[max_i+1:], n - 1)

t = 0

for b in x:
    t += int(find_largest(b, 12))

print(t)