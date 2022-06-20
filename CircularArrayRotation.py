a = [1, 2, 3]
k = 2
queries = [0, 1, 2]
len_a = len(a)
end_index = len_a - 1
shift = k % len_a
l = []
for i in range(len_a):
    l.append(i)
for i in range(len_a):
    shift_to = i + shift
    if shift_to > end_index:
        shift_to -= len_a
    l[shift_to] = a[i]
r_l = []
for q in queries:
    r_l.append(l[q])
for i in r_l:
    print(i)