def count_sides(next_num):
    # if next_num == 
    pass

def perimeter(matrix):
    # for a given 1, calculate how many sides it has
    perim = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # check all 4 sides, if a side is NOT 1, add perim
            if matrix[i][j] == 1:
                print("Before this loop: {}".format(perim))
                try:
                    if matrix[max([i,0])][max([j+1,0])] !=1: # right
                        perim += 1
                except:
                    print("except")
                    perim += 1
                print("Right: {}".format(perim))
                try:
                    if matrix[max([i+1,0])][max([j,0])] !=1: # down
                        perim += 1
                except:
                    print("except")
                    perim += 1
                print("Down: {}".format(perim))
                try:
                    if matrix[max([i,0])][max([j-1,0])] !=1: # left
                        perim += 1
                except:
                    print("except")
                    perim += 1
                print("Left: {}".format(perim))
                try:
                    if matrix[max([i-1,0])][max([j,0])] !=1: # up
                        perim += 1
                except:
                    print("except")
                    perim += 1
                print("Up: {}".format(perim))
                print("After this loop: {}".format(perim))

    return perim

result1 = perimeter([[1,0]])
# result2 = perimeter([[1,0,1], [1,1,1]])

# assert perimeter([[1,0]]) == 4
# assert perimeter([[1,0,1], [1,1,1]]) == 12
