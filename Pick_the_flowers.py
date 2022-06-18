def flower(s):
    len_s = len(s)
    dict_flower = {}
    lst = []
    max_occ = 0
    for i in range(len_s):
        if s[i] in dict_flower:
            pass
        else:
            count_ = 1
            for j in range(i + 1, len_s):
                if s[i] == s[j]:
                    count_ += 1
            dict_flower.update({s[i]: count_})
    print(dict_flower)
    max_occ = max(dict_flower.values())

    for i, j in dict_flower.items():
        if max_occ == j: 
            lst.append(ord(i))

    return(chr(min(lst)))

s = str(input())
res = flower(s)
print(res)