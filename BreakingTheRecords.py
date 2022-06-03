# given scores is consecutive games
scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]

# initialising min. and max. score as the score of first game
min_ = max_ = scores[0]

# these 2 will store the number of times she scores less than a previous games
# and the number of times she scores more than her previous game
cMin = cMax = 0

# traversing the list
for i in scores:

    # each time her score is better than her best score
    # we increement cMax
    if i > max_:

        # when score is more than max. score we update max. score with the new max. score
        max_ = i
        cMax += 1

    # each time her scores is less than her min. score
    # we increement cMin
    if i < min_:

        # when score is less than min. score we update min. score with the new min. score
        min_ = i
        cMin += 1

# at the end of the loop we know how many times she scores better than her best score
# and how many times she score less than her lowest score