d1 = 9
m1 = 6
y1 = 2015
d2 = 6
m2 = 6
y2 = 2015
fine = 0
if y1 == y2:
    if m1 == m2:
        if d1 >= d2:
            fine = 15 * (d1 - d2)
    elif m1 > m2:
        fine = 500 * (m1 - m2)
elif y1 > y2:
    fine = 10000
print(fine)