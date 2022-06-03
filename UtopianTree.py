# given different number of cycles
l = [2, 0, 1]

# a list to store height sapling reaches after going through no. of cycles
heights = []


for i in l:

    h =  1

    for j in range(1, i + 1):
        
        # starting season is spring that when j is 1, next season is summer
        # so every odd number represents spring
        if j % 2 != 0:
            
            # double height for spring
            h *= 2

        # and even represents summer
        else:

            # increase height by 1 for summer
            h += 1

    # at the end of cycles we have height which sapling has reached after the end of cycles
    heights.append(h)

# now to give desired output
for i in heights:
    print(i)