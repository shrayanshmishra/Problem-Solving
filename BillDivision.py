# no. of items eaten
n = 4

# index of the item in the list which was eaten by only one of them
k = 1

# total bill
b = 12

# list of cost of items eaten
bill = [3, 10, 2, 9]
    
# this variable will store the amount Brian owes to Anna
res = 0

# actual amount Anna has to pay
total = 0

# this for loop gets the actual amount Anna has to pay
for i in range(n):

    # we are given index value of item that Anna declines to eat
    # therefore we can skip that index when traversing the list
    if i == k:
        continue

    total += bill[i]
    # print(total, i)

# now since Brian has not declined to eat any item so he has to pay other half
# so total cost which Anna will pay will be halved also note that I've used integer division
total //= 2

# now we calculate the amount Brian owes to Anna
if b > total:
    res = b - total
else:
    res = total - b

# If he owes none then we print Bon Appetit otherwise we print the amount he owes to Anna
if res == 0:
    print("Bon Appetit")
else:
    print(res)