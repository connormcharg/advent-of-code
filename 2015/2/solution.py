r = 0
for line in open(0).read().strip().split("\n"):
    l, w, h = [int(x) for x in line.split("x")]
    # r += 2*l*w + 2*w*h + 2*h*l + min([l*w, w*h, h*l])
    r += l*w*h + 2*min([l+w, l+h, w+h])
print(r)