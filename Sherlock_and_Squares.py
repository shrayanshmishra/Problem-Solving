from math import ceil
from math import floor
from math import sqrt
a = 17
b = 24

x = sqrt(a)
y = sqrt(b)

p = ceil(x)
q = floor(y)

if a <= b:
    print(q + 1 - p)
else:
    print(0)