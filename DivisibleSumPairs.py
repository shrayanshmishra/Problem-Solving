# a sample test case
ar = [1, 3, 2, 6, 1, 2]
n = len(ar)
k = 3
c = 0
for i in range(n):
    for j in range(i + 1, n):
        if i < j and ((ar[i] + ar[j]) % k == 0):
            c += 1
print(c)