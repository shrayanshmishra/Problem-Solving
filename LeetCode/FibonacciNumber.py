n=5
a=0
b=1
print(a,'0')
print(b,'1')
k=2
for i in range(n-1):
    c=a+b
    print(c,k)
    k+=1
    a=b
    b=c
#a=0
#b=1
#c=a+b=0+1=1
#a=b
#b=c
#c=a+b=b+c=1+1