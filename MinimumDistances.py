a = [7, 1, 3, 4, 1, 7]
len_a = len(a)
min_ = 100001
for i in range(len_a - 1):
    for j in range(i + 1, len_a):
        if a[i] == a[j]:
            dist = j - i
            if dist < min_:
                min_ = dist
if min_ == 100001:
    print(-1)
else:
    print(min_)