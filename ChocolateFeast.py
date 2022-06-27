n = 6
c = 2
m = 2

new_bars = n // c

eats = 0

eats += new_bars

wrappers = 0

wrappers += eats

while True:

    new_bars = wrappers // m

    wrappers %= m
    
    eats += new_bars

    wrappers += new_bars

    if wrappers == 0:

        print(eats)
        break

    elif wrappers < m:

        print(eats)
        break