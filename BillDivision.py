n = 4
k = 1
b = 12
bill = [3, 10, 2, 9]
def bonAppetit(bill, k, b):
    res = 0
    total = 0
    for i in range(n):
        if i == k:
            continue
        total += bill[i]
        print(total, i)
    total /= 2
    total = int(total)
    if b > total:
        res = b - total
    else:
        res = total - b
    if res == 0:
        return "Bon Appetit"
    else:
        return res
res_ = bonAppetit(bill, k, b)
print(res_)
