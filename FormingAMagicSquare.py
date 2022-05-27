possMagicSquares = [[[8, 1, 6],
                     [3, 5, 7],
                     [4, 9, 2]],
                    [[6, 1, 8],
                     [7, 5, 3],
                     [2, 9, 4]],
                    [[4, 9, 2],
                     [3, 5, 7],
                     [8, 1, 6]],
                    [[2, 9, 4],
                     [7, 5, 3],
                     [6, 1, 8]],
                    [[8, 3, 4],
                     [1, 5, 9],
                     [6, 7, 2]],
                    [[4, 3, 8],
                     [9, 5, 1],
                     [2, 7, 6]],
                    [[6, 7, 2],
                     [1, 5, 9],
                     [8, 3, 4]],
                    [[2, 7, 6],
                     [9, 5, 1],
                     [4, 3, 8]]]

# a testcase from the problem
sq = [[5, 3, 4],
      [1, 5, 8],
      [6, 4, 2]]

# a variable to get total cost for converting into each of the 8 magic sqaures
costT = 0

# list to get min. cost magic sq., 'comp' for compare
comp = [] 

for i in range(8):
    for j in range(3):
        for k in range(3):
            cost = sq[j][k] - possMagicSquares[i][j][k];
            if cost < 0:
                cost *= -1
                costT += cost
            else:
                costT += cost
            # print(i, j, k)
            # print(sq[j][k], possMagicSquares[i][j][k])
            # print(cost, costT)
    comp.append(costT)
    costT = 0

# print(comp)

minCost = min(comp)

print(minCost)

# iMinCostMagicSq = comp.index(minCost)

# print(iMinCostMagicSq)

# if len(comp) == len(possMagicSquares):
#     print(True)

# minCostMagicSq = possMagicSquares[iMinCostMagicSq]

# print(minCostMagicSq)