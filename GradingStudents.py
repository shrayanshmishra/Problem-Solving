# 0 <= grade <= 100
# grade < 40, fail
# rule 1: for ex: grade = 39, 5's next multiple to 39, i.e., 40, 40 - 39, less than 3, round grade
# to 40
# rule 2: if grade < 38 no rounding
# rule 3: diff. greater or equal to 3 no rounding
# 39 // 5 = 7, a = 5 x (7 + 1)
# if 0 < a - num < 3, num = a

arr = [73, 67, 38, 33]
res = []
def gradingStudents(arr):
    for num in arr:
        a = num // 5
        b = 5 * (a + 1)
        diff = b - num
        if num > 37 and 0 < diff < 3:
            num = b
            res.append(num)
        else:
            res.append(num)
    return res
result = gradingStudents(arr)
print(result)