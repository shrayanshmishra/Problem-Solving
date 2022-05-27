s = [1, 2, 1, 3, 2]
d = 3
m = 2
c = 0
# for i in range(0, len(s)):
#     for j in range(i + 1, len(s) + 1):
#         a = s[i: j]
#         if sum(a) == d and len(a) == m:
#             c += 1
# print(c)

for i in range(len(s) - m + 1):
    a = s[i: i + m]
    if sum(a) == d:
        c += 1
print(c)