# taking a string input to the time and format
s1 = "12:09:43PM"
    
# now we need the integer time values and AM PM without the colon to operate properly for time conversion
# so split them where you find colon, hence s2 will be ['12', '09', '43PM']
# and we only need to operate with s2[0] that is hr, and the format that is in s2[2]
s2 = s1.split(":")

# output is needed as string, so convert and keep adding the needed time and format to this string
res = ""

# testcase 1: if it 12:00:00AM or 12:00:00PM
if "12" in s1:

    # when it is 12:00:00AM we have to give output 00:00:00 in 24 hr format
    if "AM" in s1:

        # a string which will separate time and format
        s3 = s2[2].split("AM")
        s3 = s3[0]

        # here almost its done 12 that was in AM formate is now replaced with 00 of 24 hr format
        s2[0] = "00"

        # now to convert it into proper string output as we need it with colons
        res = s2[0] + ":" + s2[1] + ":" + str(s3)

    elif "PM" in s1:
        # when it is 12:00:00PM we have to give output 12:00:00 in 24 hr format so just remove PM
        s3 = s2[2].split("PM")
        s3 = s3[0]

        res = s2[0] + ":" + s2[1] + ":" + str(s3)
else:
    # if time is in am and does not include noon time that is 12 in AM or PM simply remove AM
    if "AM" in s1:
        s3 = s2[2].split("AM")
        s3 = s3[0]
        res = s2[0] + ":" + s2[1] + ":" + str(s3)

    # when time is in PM but does not include 12 for example 6:09:22PM so we need to return 18:09:22 so remove PM convert 6 which is in
    # string to integer add 12 to 6
    if "PM" in s1:
        s3 = s2[2].split("PM")
        s3 = s3[0]
        a = int(s2[0])
        a += 12
        res = str(a) + ":" + s2[1] + ":" + str(s3)

# time in 24 hr format
print(res)