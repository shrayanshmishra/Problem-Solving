# let's say given number is 93212
num = -121

# to check if rev. of number is read same as number we'll type cast the number to a string
# then we'll traverse the string in rev. direction and in forward direction at the same time
# and check equality of elements

str_num = str(num)

# it is given that input can be -ve or +ve, so when input will be -ve it won't be a palindrome
if '-' in str_num:

    condition = False
    palindrome = "false"
    print(palindrome)

else:

    len_str_num = len(str_num)

    # when length of string is even loop will run half the length times, when length of string is odd
    # loop will run (length + 1) / 2 times

    if len_str_num % 2 == 0:

        loop = len_str_num // 2

    else:

        loop = (len_str_num + 1) // 2

    condition = False

    j = 0

    for i in range(-1, -(loop + 1), -1):

        if str_num[j] == str_num[i]:

            condition = True

        else:

            condition = False
            break

        j += 1

    palindrome = "false"

    if condition:

        palindrome = "true"

    else:

        palindrome = "false"

    print(palindrome)