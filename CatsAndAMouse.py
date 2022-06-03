posCatA = 9
posCatB = 7
posMouse = 5

distCatA = posCatA - posMouse
distCatB = posCatB - posMouse

if distCatA < 0:
    distCatA *= -1

if distCatB < 0:
    distCatB *= -1

if distCatA == distCatB:
    print("Mouse C")
elif distCatA < distCatB:
    print("Cat A")
else:
    print("Cat B")