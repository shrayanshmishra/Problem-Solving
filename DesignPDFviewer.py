# since we need to know height of alphabets according to heights list given
# therefore i am creating a list with all 26 alphabets
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

len_alphabets = 26
word = "abc"

# we'll need the length of word to find highlighted area
len_word = len(word)

# whatever heights list will be given for alphabets
heights = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

# a variable to get alphabet with max. height
max_height = 0

# now for each letter in word we are running a linear search for loop
# this linear search will compare and update max. height
for i in word:
    for j in range(len_alphabets):
        if i == alphabets[j]:

            # since both heights list and alphabets list have same length
            # index will be same, so no need for another variable here
            if max_height < heights[j]:
                max_height = heights[j]

# at the end of the nested for we'll get alphabet with max. height
# hence we can find how much area is to be highlighted
area = max_height * len_word

# highlighted area
print(area)