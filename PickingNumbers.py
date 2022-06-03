a = [4, 6, 5, 3, 3, 1]

# better to sort so that everything below runs properly
# if you don't sort everything below is wrong...
a.sort()

# length of array
l1 = len(a)

# a list to store all subarrays
List = []

# generating all subarrays
for i in range(l1):
    for j in range(i + 1, l1 + 1):
        subArr = a[i: j]
        
        if subArr in List:
            pass
        else:
            List.append(a[i: j])

# print(List)

# length of 'List' list 
l2 = len(List)

# a list where we'll append the needed subarrays
neededSAs = []

for i in range(l2):
    
    # subarrays
    subArr = List[i]

    # length of subArr
    lSA = len(subArr)

    # thess two boolean variables will help us to get all subarrays
    # and also will help us to come out from the nested loop below
    # which satisfy the need of this problem and then we'll
    # find the longest subarray from all those subarrays
    condition = False
    isSubArr = False

    # nested loop checking all possible combinations of one element
    # encountering another element in a subarray
    for i in range(lSA - 1):
        for j in range(i + 1, lSA):
            Diff = subArr[i] - subArr[j]
            # print(Diff)
            if Diff < 0:
                Diff *= -1
            if Diff == 0 or Diff == 1:
                # print(Diff)
                isSubArr = True
            else:
                isSubArr = False
                break
        if isSubArr:
            condition = True
        else:
            condition = False
            break

    # if condition is satisfied we'll append in 'neededSAs'
    if condition:
        # print(subArr)
        neededSAs.append(subArr)

print(neededSAs)

# longest subarray which satisfies the condition
longestSA = []

# a variable to find which subarray has most no. of elements
highestLength = len(neededSAs[0])

for i in range(1, len(neededSAs)):

    # print(highestLength)

    # a temporary variable to compare lengths of subarrays
    temp = len(neededSAs[i])

    if temp > highestLength:
        highestLength = temp

print(highestLength)