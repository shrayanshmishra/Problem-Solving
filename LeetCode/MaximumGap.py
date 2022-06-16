nums = [3, 6, 9, 1]

nums.sort()

len_nums = len(nums)

max_sum = 0

for i in range(len_nums - 1):

    j = i + 1

    sum_cons = 0
    sum_cons = nums[i] - nums[j]

    if sum_cons < 0:

        sum_cons *= -1

    if sum_cons > max_sum:

        max_sum = sum_cons