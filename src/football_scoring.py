"""
Given possible point gains of [2,3,6,7,8]
How many ways are there to score N points
Same as coin problem
"""

scores = [2,3,6,7,8]


def football(n, scores):
    # Create the ways array to 1 plus the amount 
    # to stop overflow 
    ways = [0] * (n+1)

    # Set the first way to 1 because its 0 and 
    # there is 1 way to make 0 with 0 coins 
    ways[0] = 1
    
    # Go through all of the coins 
    for i in range(len(scores)):

        # Make a comparison to each index value 
        # of ways with the coin value. 
        for j in range(len(ways)):
            if (scores[i] <= j):

                # Update the ways array
                ways[j] += ways[(int)(j-scores[i])]
                
    # return the value at the Nth position 
    # of the ways array. 
    return ways[n]

print(football(10, scores))