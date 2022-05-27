ar = [1, 3, 2, 6, 1, 2]
n = len(ar)
k = 3
c = 0
for i in range(n):
    for j in range(1, n):
        if i >= j:
            pass
        else:
            # print(i, j)
            if i < j and ((ar[i] + ar[j]) % k == 0):
                # print(i, j, ar[i], ar[j], ar[i] + ar[j])
                c += 1
print(c)