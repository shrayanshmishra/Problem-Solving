nums = [2, 7, 11, 15]
target = 9
lN = len(nums)
lst = []
condition = ""
for i in range(lN - 1):
    for j in range(i + 1, lN):
        if nums[i] + nums[j] == target:
            lst = [i, j]
            condition = "satisfied"
            break
    if condition == "satisfied":
        break
print(lst)