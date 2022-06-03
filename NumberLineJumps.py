x1 = 21
x2 = 47
v1 = 6
v2 = 3
def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 < v2:
        return "NO"
    elif x1 > x2 and v1 > v2:
        return "NO" 
    elif x1 == x2 and v1 == v2:
        return "YES"
    elif x1 != x2 and v1 == v2:
            return "NO"
    elif x1 == x2 and v1 != v2:
        return "NO"
    elif x1 < x2 and v1 > v2:
        i = 1
        while True:
            if x1 > x2:
                return "NO"
            elif x1 == x2:
                return "YES"
            else:
                x1 += v1 * i
                x2 += v2 * i
    elif x1 > x2 and v1 < v2:
        i = 1
        while True:
            if x1 < x2:
                return "NO"
            elif x1 == x2:
                return "YES"
            else:
                x1 += v1 * i
                x2 += v2 * i
res = kangaroo(x1, v1, x2, v2)
print(res)