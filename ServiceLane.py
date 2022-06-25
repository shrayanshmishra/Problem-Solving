width = [2, 3, 1, 2, 3, 2, 3, 3]
cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
l = []
for i in range(len(cases)):
    x = cases[i]
    a = x[0]
    b = x[1]
    c = width[a: b + 1]
    l.append(min(c))
print(l)