lst = []
for i in range(97, 123):
    lst.append(chr(i))
len_lst = len(lst)
word = "abc"
len_word = len(word) 
heights = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
max_height = 0
for i in word:
    for j in range(len_lst):
        if i == lst[j]:
            if max_height < heights[j]:
                max_height = heights[j]
area = max_height * len_word
print(area)