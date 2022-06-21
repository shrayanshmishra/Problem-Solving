c = [0, 0, 1, 0, 0, 1, 1, 0]
k = 2
i = 0
e = 100
while True:
    len_c = len(c)
    i = (i + k) % len_c
    e -= 1
    if c[i] == 1:
        e -= 2
    if i == 0:
        break
print(e)