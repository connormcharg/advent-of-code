from hashlib import md5

x = open(0).read().strip()
i = 1
input = x + str(i)
while not (md5(input.encode()).hexdigest().startswith("000000")):
    i += 1
    input = x + str(i)
print(i)