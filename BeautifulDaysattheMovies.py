beautifulDays = []

# this is i passed to the function
l = 20

# this is j passed to the function, I've hard coded both of them with a sample test case
u = 23

k = 6

for i in range(l, u + 1):

    # convert the integer number to string
    s1 = str(i)

    s2 = ""
    len_s1 = len(s1)
    j_up_lim = -(len_s1 + 1)

    # then append the string backwards to another string variable
    for j in range(-1, j_up_lim, -1):
        s2 += s1[j]

    # convert this string variable to integer
    m = int(s2)

    # take difference between number and its reverse number
    d = i - m

    # if its negative make it positive
    if d < 0:
        d *= -1

    # check if the difference is divisible by given k value
    div_chk = d % k

    # if it is divisible append to a list
    if div_chk == 0:
        beautifulDays.append(i)

# finally you've have a list find its length
len_beautifulDays = len(beautifulDays)

# print the length, as you have to tell no. of beautiful days number in the i, j range
print(len_beautifulDays)