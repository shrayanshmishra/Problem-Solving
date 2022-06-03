noOfPages = int(input())
pageToReach = int(input())

if noOfPages % 2 == 0:
    noOfPages += 1

minPgTrnFrnt = pageToReach // 2
minPgTrnBck = (noOfPages - pageToReach) // 2

print(minPgTrnFrnt, minPgTrnBck, min(minPgTrnFrnt, minPgTrnBck))