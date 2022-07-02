def appendAndDelete(s, t):

    res = "No"

    if k >= len(s) + len(t):
        res = "Yes"
    else:
        len_s = len(s)
        len_t = len(t)
        
        can_red = False
        
        s_list = list(s)
        t_list = list(t)
        
        i = -1
        
        if len_s > len_t:
        
            for i in range(-1, -len(s), -1):
                
                if s[: len(s_list)] == t[: len(s_list)]:
                    i += len_s
                    break
            
                s_list.pop()
                
                k -= 1        

        if s_list == t_list and k >= 0 and k % 2 == 0:
            res = "Yes"
            return res
            
        if len(s_list) == 0:
            can_red = True

        i += 1
        
        if len(s_list) < len(t_list):
        
            while s_list != t_list:
                
                if i == len_t:
                    break
                
                s_list.append(t_list[i])
                i += 1
                k -= 1

        if s_list == t_list and (k >= 0 and k % 2 == 0):
            res = "Yes"
            return res
            
        if can_red and k > 0:
            if s_list == t_list:
                res = "Yes"
        elif k == 0:
            if s_list == t_list:
                res = "Yes"

    return res