# given list of numbers
nums = [2, 7, 11, 15]

# given value of target
target = 9

# 'lN' for length of nums list
lN = len(nums)

# a list where we'll store the indices of the two numbers
lst = []

# a string variable to update situation if condition is satisfied
# but major reason is to break out of the nested for loop 
condition = ""

# a nested for loop to check each combination
for i in range(lN - 1):
    for j in range(i + 1, lN):

        # checking if condition is satisfied or not
        if nums[i] + nums[j] == target:
            lst = [i, j]

            # update the condition variable if condition is satisfied
            condition = "satisfied"

            # no need to check anymore since it is specified in the problem
            # that only 1 pair of numbers satisfies the condition
            break

    # since its a nested loop so we need 2 break statements to come out
    if condition == "satisfied":
        break

# finally we can print the indices of the two numbers
print(lst)