# possible 3 x 3 magic squares
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

# since possible magic square for a 3 x 3 sqaure are only 8
# so the length for first loop is 8
for i in range(8):

    # nested for loop for checking with each of the 8 magic sqaures and calculating cost
    # of converting the 3 x 3 square into a magic square
    for j in range(3):
        for k in range(3):

            # this variable finds cost of replacing the elements
            cost = sq[j][k] - possMagicSquares[i][j][k];

            # to get total cost of changing the square into magic square 
            if cost < 0:

                # since in question it is cleary mentioned that cost is non - negative
                # so if it is negative we'll make it positive and keep totalling the cost
                cost *= -1
 
                # this costT variable is keeping total cost of changing the square into magic square 
                costT += cost
            else:
                costT += cost

    # comp for compare this comp is a list which'll hold cost of changing square into magic square for
    # each of the magic squares, from this we'll get the min. cost of changing the square into magic square
    comp.append(costT)
    costT = 0

# min. cost of changing the square into magic square
minCost = min(comp)

# print min. cost of changing the sqaure into magic square
print(minCost)