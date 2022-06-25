a = [1, 2, 3, 4, 3, 3, 2, 1]

l = []

while len(a) > 0: 

    x = min(a)
    
    l.append(len(a))
    
    for i in range(len(a)):

        a[i] -= x


    while 0 in a:
        
        a.remove(0)

for i in l:

    print(i)