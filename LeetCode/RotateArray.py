def rotate(nums, k):
    len_nums = len(nums)
    k %= len_nums
    x = nums[len_nums - k: len_nums]
    y = nums[: len_nums - k]
    nums.clear()
    nums.extend(x)
    nums.extend(y)
    print(nums)