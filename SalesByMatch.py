# length of the socks list
sizeOfSocksArr = 9

# given color identified by numbers, of socks in a pile
socksArr = [10, 20, 20, 10, 10, 30, 50, 10, 20]

# a dictionary to map the color with no. of socks
dictColSocks = {}

# for every color
for i in range(sizeOfSocksArr):

    # if a color has already been update with how many of its colors are present we move to next color
    # cause we don't want any repitition so that we have return exact no. of pairs that can be made 
    if socksArr[i] in dictColSocks:
        pass
    else:
        
        # a counter to count the number of socks of same color
        noOfSocks = 1
        for j in range(i + 1, sizeOfSocksArr):
            
            # whichever color we encounter while traversing we start counting no. of socks of that color
            if socksArr[i] == socksArr[j]:
                
                # incrementing counter thereby counting total no. of socks
                noOfSocks += 1

        # the array is traversed and we've counter the 
        dictColSocks.update({socksArr[i]: noOfSocks})

# to store total pairs that we can have of the socks while pairing same color socks together
totalPairs = 0

# now for the no. of socks available of each color
for i in dictColSocks.values():

    # to check if pair can be made or not by checking remainder after dividing by 2
    pairChk = 0
    
    # pairs possible for each color
    pairs = 0

    pairChk = i % 2
    
    if pairChk == 0:
        
        pairs = i // 2
        totalPairs += pairs
    
    else:
        
        i -= pairChk
        pairs = i // 2
        totalPairs += pairs

# total pairs    
print(totalPairs)