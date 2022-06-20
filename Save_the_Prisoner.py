n = 4
m = 6
s = 2
x = m % n
s += x - 1
while s > n or s == 0:
    if s == 0:
        s += n
    else:
        s -= n    
print(s)