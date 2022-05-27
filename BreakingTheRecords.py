scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
# def breakingRecords(scores):
min_ = max_ = scores[0]
cMin = cMax = 0
for i in scores:
    if i > max_:
        max_ = i
        cMax += 1
    if i < min_:
        min_ = i
        cMin += 1
    print(scores, i, max_, min_, cMax, cMin)
#     return cMax, cMin
# res = breakingRecords(scores)
# print(res)