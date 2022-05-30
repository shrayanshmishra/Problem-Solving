# given hurdles' heights
height = [1, 1, 1, 1, 1]

# given character's jumping capacity
k = 1

# find max. height from hurdles' heights
maxHeight = max(height)

noOfDoses = 0

if k < maxHeight:
    noOfDoses = maxHeight - k
print(noOfDoses)