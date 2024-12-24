import math

nums = list(map(int, open(0).read().splitlines()))
prices = []

for i in range(len(nums)):
    prices.append([int(str(nums[i])[-1])])
    for _ in range(2000):
        nums[i] ^= (nums[i] * 64)
        nums[i] %= 16777216
        nums[i] ^= math.floor(nums[i] / 32)
        nums[i] %= 16777216
        nums[i] ^= (nums[i] * 2048)
        nums[i] %= 16777216
        prices[i].append(int(str(nums[i])[-1]))

map = {}
seen_seq = set()

for i in range(len(prices)):
    for j in range(len(prices[i]) - 4):
        if i not in map:
            map[i] = {}
        seq = (
            prices[i][j+1] - prices[i][j],
            prices[i][j+2] - prices[i][j+1],
            prices[i][j+3] - prices[i][j+2],
            prices[i][j+4] - prices[i][j+3]
        )
        if seq not in map[i]:
            map[i][seq] = prices[i][j+4]
        seen_seq.add(seq)

m = -1

for s in seen_seq:
    t = 0
    for k in map.keys():
        if s in map[k]:
            t += map[k][s]
    if t > m:
        m = t

print(m)