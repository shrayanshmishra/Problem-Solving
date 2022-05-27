s1 = "12:09:43PM"
def timeConversion(s1):
    s2 = s1.split(":")
    l = len(s2)
    res = ""
    if "12" in s1:
        if "AM" in s1:
            s3 = s2[l - 1].split("AM")
            s3 = s3[0]
            s2[0] = "00"
            res = s2[0] + ":"
            for i in range(1, l - 1):
                res += s2[i] + ":"
            res += str(s3)
        elif "PM" in s1:
            s3 = s2[l - 1].split("PM")
            s3 = s3[0]
            for i in range(0, l - 1):
                res += s2[i] + ":"
            res += str(s3)
    else:
        if "AM" in s1:
            s3 = s2[l - 1].split("AM")
            s3 = s3[0]
            for i in range(0, l - 1):
                res += s2[i] + ":"
            res += str(s3)
        if "PM" in s1:
            s3 = s2[l - 1].split("PM")
            s3 = s3[0]
            a = int(s2[0])
            a += 12
            res = str(a) + ":"
            for i in range(1, l - 1):
                res += s2[i] + ":"
            res += str(s3)
    return res
result = timeConversion(s1)
print(result)