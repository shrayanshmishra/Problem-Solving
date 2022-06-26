# min. no of elements to delete to leave only elements of equal value
# check occurence of every no.
# iterate every key value leaving current
# the min. is answer

arr = [1, 2, 2, 3]

dict_for_arr = {}

arr.sort()

len_arr = len(arr)

for i in range(len_arr - 1):

    c = 1

    if arr[i] not in dict_for_arr.keys():

        for j in range(i + 1, len_arr):

            if arr[i] == arr[j]:

                c += 1

        dict_for_arr.update({arr[i]: c})

if arr[len_arr - 1] not in dict_for_arr.keys():

    dict_for_arr.update({arr[len_arr - 1]: 1})

min_del = sum(dict_for_arr.values())

for i in dict_for_arr.keys():

    a = 0

    for j, k in dict_for_arr.items():

        if j != i:

            a += k

    if a < min_del:
    
        min_del = a

print(min_del)