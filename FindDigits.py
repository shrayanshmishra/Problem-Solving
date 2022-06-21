n = 1012
str_n = str(n)
no_of_divisors = 0
for i in str_n:
    int_i = int(i)
    if int_i == 0:
        pass
    elif n % int_i == 0:
        no_of_divisors += 1
print(no_of_divisors)