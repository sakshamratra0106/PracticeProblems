# https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/

# Python program to count all possible paths
# from top left to bottom right

# function to return count of possible paths
# to reach cell at row number m and column
# number n from the topmost leftmost
# cell (cell at 1, 1)
def numberOfPaths(m, n):
    """

    :param m:
    :param n:
    :return:

    The time complexity of above recursive solution is exponential.
    """
    # If either given row number is first
    # or given column number is first
    if m == 1 or n == 1:
        return 1

    # If diagonal movements are allowed
    # then the last addition
    # is required.
    return numberOfPaths(m - 1, n) + numberOfPaths(m, n - 1)


# Driver program to test above function
m = 3
n = 3
print(numberOfPaths(m, n))

# This code is contributed by Aditi Sharma


# Python program to count all possible paths
# from top left to bottom right

# Returns count of possible paths to reach cell
# at row number m and column number n from the
# topmost leftmost cell (cell at 1, 1)
def numberOfPaths(m, n):
    # Create a 2D table to store
    # results of subproblems
    # one-liner logic to take input for rows and columns
    # mat = [[int(input()) for x in range (C)] for y in range(R)]

    count = [[0 for x in range(n)] for y in range(m)]

    # Count of paths to reach any
    # cell in first column is 1
    for i in range(m):
        count[i][0] = 1;

    # Count of paths to reach any
    # cell in first column is 1
    for j in range(n):
        count[0][j] = 1;

    # Calculate count of paths for other
    # cells in bottom-up
    # manner using the recursive solution
    for i in range(1, m):
        for j in range(1, n):
            count[i][j] = count[i - 1][j] + count[i][j - 1]
    return count[m - 1][n - 1]


# Driver program to test above function
m = 3
n = 3
print(numberOfPaths(m, n))

# This code is contributed by Aditi Sharma