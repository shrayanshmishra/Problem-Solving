numbers = [1, 4, 4, 4, 5, 3]
length = len(numbers)

# a dictionary is significant since it can take birds' ids as keys and map these ids as keys to
# values which will be the no. of times the birds were sighted
dictNum = {}

# traversing the birds' ids
for i in range(length):

    # to prevent repetitive dictionary updation of same bird's frequency of being sighted
    if numbers[i] in dictNum:
        pass
    else:

        # a counter to count the number of time bird was sighted
        e = 1

        # check number of times it was sighted
        for j in range(i + 1, length):
            
            # if an id is occuring again and again we count the no. of times it was seen
            if numbers[i] == numbers[j]:
                e += 1

        # update dictionary with bird and no. of times it was seen
        dictNum.update({numbers[i]: e})

# this list will contain the birds which were seen the most no. of times
listFinal = []

# finding what no. of times was the maximum
maxFreq = max(dictNum.values())

# iterating over dictionary key value pairs to get birds' ids and append to listFinal
for i, j in dictNum.items():
    if j == maxFreq:
        listFinal.append(i)

# bird's id which was sighted most no. of times and also which has the least value of id
min_id = min(listFinal)

print(min_id)