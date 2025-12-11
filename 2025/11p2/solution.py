from collections import deque

x = {a.split(": ")[0]: a.split(": ")[1].split(" ") for a in open(0).read().splitlines()}

memo = {}

def count_paths(current, target):
    if current == target:
        return 1
    
    if (current, target) in memo:
        return memo[(current, target)]
    
    count = 0
    if current in x:
        for nxt in x[current]:
            count += count_paths(nxt, target)
    
    memo[(current, target)] = count
    return count

paths_svr_to_fft = count_paths("svr", "fft")
paths_svr_to_dac = count_paths("svr", "dac")
paths_fft_to_dac = count_paths("fft", "dac")
paths_dac_to_fft = count_paths("dac", "fft")
paths_fft_to_out = count_paths("fft", "out")
paths_dac_to_out = count_paths("dac", "out")

total = 0
total += paths_svr_to_fft * paths_fft_to_dac * paths_dac_to_out
total += paths_svr_to_dac * paths_dac_to_fft * paths_fft_to_out

print(total)