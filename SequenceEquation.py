p = [4, 3, 5, 1, 2]
len_p = len(p)
l1 = []
for x in range(1, len_p + 1):
    print("x:", x)
    for i in range(len_p):
        print("p[i]:", p[i])
        if p[i] == x:
            l1.append(i + 1)
            break
        print("l1:", l1)
print("end1")
l2 = []
for x in l1:
    print("x:", x)
    for i in range(len_p):
        print("p[i]:", p[i])
        if p[i] == x:
            l2.append(i + 1)
            break
print(l2)