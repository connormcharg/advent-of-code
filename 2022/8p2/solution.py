x = open(0).read().splitlines()

m = -1

for i in range(1, len(x) - 1):
    for j in range(1, len(x[i]) - 1):
        y = int(x[i][j])
        down = 0
        up = 0
        right = 0
        left = 0
        for a in range(i+1, len(x)):
            down += 1
            if int(x[a][j]) >= y:
                break
        for a in range(i-1, -1, -1):
            up += 1
            if int(x[a][j]) >= y:
                break
        for a in range(j+1, len(x[i])):
            right += 1
            if int(x[i][a]) >= y:
                break
        for a in range(j-1, -1, -1):
            left += 1
            if int(x[i][a]) >= y:
                break
        m = max(m, down*up*left*right)
        
print(m)