low = 13
high = 22

x = high - low

if low % 2 == 1:
	x += 1
	if high % 2 == 0:
		x -= 1
elif high % 2 == 0:
	x -= 1

if x % 2 == 0:
	print(x//2)
else:
	print((x + 1)//2)