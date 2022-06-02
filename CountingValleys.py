# given no. of steps taken by the hiker or you can say length of path list is given
steps = int(input())

# given movement of the hiker as a string containg D or U, whether he takes next step up or down
path = str(input())

# now to keep count of no. of valleys hiker encounter a variable
noOfValleys = 0

# notice what the problem says
# a valley starts when the hiker steps down from sea level and the valleys only ends when he comes up again to sea level
verticalPos = []

# so basically he'll always start from sea level, we just have to see when he steps up to the sea level again
vertical = 0

for i in range(steps):
    if path[i] == 'D':
        vertical -= 1
        verticalPos.append(vertical)
    else:
        vertical += 1
        verticalPos.append(vertical)

    # this is the condition where we check if it was a valley or not based on whether hiker step up to sea level or not
    if verticalPos[i] == 0 and verticalPos[i - 1] < 0:
        noOfValleys += 1

print(noOfValleys)