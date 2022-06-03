# 0 <= grade <= 100
# grade < 40, fail
# rule 1: for ex: grade = 39, 5's next multiple to 39, i.e., 40, 40 - 39, less than 3, round grade
# to 40
# rule 2: if grade < 38 no rounding
# rule 3: diff. greater or equal to 3 no rounding
# 39 // 5 = 7, a = 5 * (7 + 1)
# if 0 < a - num < 3, num = a

# marks of a student
arr = [73, 67, 38, 33]

# rounded off marks
res = []

def gradingStudents(arr):
    for num in arr:

        # gives value of nth multiple closes to the marks in a subject
        a = num // 5
        
        # a + 1 will give next n closest to a
        # thus b which is equal to 5 * (a + 1) will give next multiple of 5
        b = 5 * (a + 1)

        # difference between next multiple and marks
        diff = b - num

        # if marks are equal or greater to 38 then student is pass
        # and rounding is done only when difference is less than, and since 0 difference has no significance here
        # thus the following if condition
        # reason why num > 37 is used, since 38 and 39 are close to 40, and difference is less than 3, they will be
        # rounded to 40 also 40 marks is considered as pass, thus the condition
        if num > 37 and 0 < diff < 3:

            # if both conditions are satisfies rounding is done
            num = b
            res.append(num)
        else:

            # otherwise nothing is done
            res.append(num)

    # marks after checking
    return res
result = gradingStudents(arr)
print(result)