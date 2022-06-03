# a sample test case
a = [2, 4]
b = [24, 36]

# and no need to sort a and b, they are already sorted

len_b = len(b)
last_index_of_b = len_b - 1
c = b[last_index_of_b] + 1
arr1 = []
arr2 = []

# for every number in the inclusive range 2, 36
for i in range(a[0], c):

    # a boolean flag variable
    d = True

    # for every number of a
    for j in a:

        # if it divides i
        if i % j == 0:
            pass
        else:
            d = False
    
    # then d remains true and we append it to arr1
    if d:
        arr1.append(i)

# now for every number in arr1
for i in arr1:

    # again a boolean flag variable
    d = True

    # for every number in b
    for j in b:

        # if i divides j
        if j % i == 0:
            pass
        else:
            d = False

    # then d remains true and we append it to arr2
    if d:
        arr2.append(i)

# length of arr2
len_arr2 = len(arr2)

# print length
print(len_arr2)

# since we were asked to tell how many such numbers are there which divide every element in b and are divisible by every
# number in a in the inclusive range smallest number of 'a' and largest number of 'b' we iterated a for loop for every
# number in the inclusive range smallest number of 'a' and largest number of 'b' and check if it is divisbile by every
# number in 'a', then we check these number if they divide every number in b or not then the numbers which satisfy both
# condition we append them to list arr2 and find the length of this list to know how many such number are there