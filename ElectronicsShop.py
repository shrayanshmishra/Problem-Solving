budget = 374625
keyboardVar = 797
usbVar =  951
keyboards = list(map(int, input().rstrip().split())) # [40, 50, 60]
usbs = list(map(int, input().rstrip().split())) # [5, 8, 12]

maxBuy = 0
buyChkAr = []

for kb in keyboards:
    for usb in usbs:
        if kb < budget and usb < budget:
            if kb + usb <= budget:
                maxBuy = kb + usb
                buyChkAr.append(maxBuy)

if buyChkAr:            
    print(max(buyChkAr))
else:            
    print(-1)