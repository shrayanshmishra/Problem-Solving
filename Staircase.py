# this loop can print multiple rows
for i in range(4):

    # a nested loop is needed to print multiple columns
    for j in range(4):

        # this condition is the crux of this problem
        # when you'll add the index values of places where # is printed
        # you'll also observe this relation
        if i + j >= 3:
            
            # this line will print # without gap
            print("#", end="")
        else:
            # this will indent the hashes
            print(" ", end="")
    # this will change the lines that is create multiple rows, otherwise output will be in a
    # single line
    print()