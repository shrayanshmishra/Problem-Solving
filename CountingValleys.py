steps = int(input())
path = str(input())

noOfValleys = 0
verticalPos = []
vertical = 0

for i in range(steps):
    if path[i] == 'D':
        vertical -= 1
        verticalPos.append(vertical)
    else:
        vertical += 1
        verticalPos.append(vertical)
    if verticalPos[i] == 0 and verticalPos[i - 1] < 0:
        noOfValleys += 1

print(noOfValleys)