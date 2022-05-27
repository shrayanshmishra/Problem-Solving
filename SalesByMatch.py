sizeOfSocksArr = 9 # n
socksArr = [10, 20, 20, 10, 10, 30, 50, 10, 20] # ar
dictColSocks = {}
for socksCol in range(sizeOfSocksArr):
    if socksArr[socksCol] in dictColSocks:
        pass
    else:
        noOfSocks = 1
        for j in range(socksCol + 1, sizeOfSocksArr):
            if socksArr[socksCol] == socksArr[j]:
                noOfSocks += 1
                # print(socksCol, nxtSockCol, noOfSocks)
        dictColSocks.update({socksArr[socksCol]: noOfSocks})
print(dictColSocks)
totalPairs = 0
for socksCol in dictColSocks.values():
    pairChk = 0
    pairs = 0
    pairChk = socksCol % 2
    # print(pairChk, pairs, socksCol)
    if pairChk == 0:
        pairs = socksCol // 2
        totalPairs += pairs
    else:
        socksCol -= pairChk
        pairs = socksCol // 2
        totalPairs += pairs
    # print(pairChk, pairs, socksCol)
print(totalPairs)