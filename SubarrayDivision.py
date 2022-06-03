s = [1, 2, 1, 3, 2]
d = 3
m = 2
c = 0

for i in range(len(s) - m + 1):
    a = s[i: i + m]
    if sum(a) == d:
        c += 1
print(c)