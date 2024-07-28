x = open(0).read().split("\n")
blocks = []
temp = []
for line in x:
    if line == "":
        blocks.append(temp)
        temp = []
        continue
    temp.append(line)

def check_row(block, row):
    if row == 0:
        return block[0] == block[1]

    for i in range(row + 1):
        row_to_check = (row - i) + (row + 1)
        if row_to_check >= len(block):
            continue
        if block[i] != block[row_to_check]:
            return False
    return True

def check_col(block, col):
    if col == 0:
        for i in range(len(block)):
            if block[i][0] != block[i][1]:
                return False
        return True

    for i in range(col + 1):
        col_to_check = (col - i) + (col + 1)
        if col_to_check >= len(block[0]):
            continue
        for j in range(len(block)):
            if block[j][i] != block[j][col_to_check]:
                return False
    return True

def get_total(block):
    total = 0
    for row in range(len(block)-1):
        if check_row(block, row):
            total += (row + 1) * 100
    for col in range(len(block[0])-1):
        if check_col(block, col):
            total += (col + 1)
    return total

total = 0

for block in blocks:
    total += get_total(block)

print(total)