# given heights of candles
arr = [3, 2, 1, 3]

# to store the no. of candles having highest height
c = 0
for i in arr:

    # using python in-built function to find highest height
    # and if any candle has height equal to max. height
    # counter is increemented
    if i == max(arr):
        c += 1

# candles having highest height
print(c)