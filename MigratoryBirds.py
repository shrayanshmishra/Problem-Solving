numbers = [1, 4, 4, 4, 5, 3]
length = len(numbers)
dictNum = {}
for i in range(length):
    if numbers[i] in dictNum:
        pass
    else:
        e = 0
        for j in range(i + 1, length):
            if numbers[i] == numbers[j]:
                e += 1
                print(i, j, e)
        dictNum.update({numbers[i]: e})
print(dictNum)
listFinal = []
maxFreq = max(dictNum.values())
for i, j in dictNum.items():
    if j == maxFreq:
        listFinal.append(i)
print(min(listFinal))