# given arrival times of all students
a = [-1, -6, 8, 3, 0, -5]

# no. of students
n = len(a)

# threshold no. of students
k = 4

kcount = 9

cancel_class = "YES"

for i in range(n):

    if a[i] <= 0:

        # count no. of students who came on time
        kcount += 1

        # if students are equal  to threshold no. of students then no cancellation of class
        if kcount == k:

            cancel_class = "NO"
            break

print(cancel_class)