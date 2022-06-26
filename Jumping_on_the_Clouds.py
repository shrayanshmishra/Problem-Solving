c = [0, 0, 0, 1, 0, 0]
len_c = len(c)
i = 0
jumps = 0
while i < len_c:
    if i + 2 < len_c and c[i + 2] == 0:
        jumps += 1
        i += 2
    elif i + 1 < len_c and c[i + 1] == 0:
        jumps += 1
        i += 1
    else:
        break
print(jumps)