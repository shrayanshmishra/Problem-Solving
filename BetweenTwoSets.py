a = [2, 4]
b = [24, 36]
def getTotalX(a, b):
    a.sort()
    b.sort()
    c = b[len(b) - 1] + 1
    arr1 = []
    arr2 = []
    for i in range(a[0], c):
        d = True
        for j in a:
            if i % j == 0:
                pass
            else:
                d = False
        if d:
            arr1.append(i)
    arr1.sort()
    for i in arr1:
        d = True
        for j in b:
            if j % i == 0:
                pass
            else:
                d = False
        if d:
            arr2.append(i)
    return len(arr2)
res = getTotalX(a, b)
print(res)