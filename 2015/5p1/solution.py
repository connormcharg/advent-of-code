from string import ascii_lowercase
d = [x+x for x in list(ascii_lowercase)]
x = open(0).read().strip().split("\n")
t = 0
for line in x:
    if any([x in line for x in ["ab", "cd", "pq", "xy"]]):
        continue
    if not any([x in line for x in d]):
        continue
    if not (sum([1 for letter in line if letter in "aeiou"]) >= 3):
        continue
    t += 1
print(t)