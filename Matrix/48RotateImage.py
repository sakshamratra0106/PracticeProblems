"""
https://leetcode.com/problems/rotate-image/
https://leetcode.com/problems/rotate-image/solution/
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """

        :param matrix:
        :return:

        Complexity Analysis

        Let MM be the number of cells in the matrix.

        Time complexity : O(M), as each cell is getting read once and written once.

        Space complexity : O(1) because we do not use any other additional data structures.

        """
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp

    def rotate1(self, matrix: List[List[int]]) -> None:
        """

        :param matrix:
        :return:

        Complexity Analysis

        Let MM be the number of cells in the grid.

        Time complexity : O(M). We perform two steps; transposing the matrix, and then reversing each row.
        Transposing the matrix has a cost of O(M) because we're moving the value of each cell once.
        Reversing each row also has a cost of O(M), because again we're moving the value of each cell once.

        Space complexity : O(1) because we do not use any other additional data structures.

        """
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate1(matrix)
    print("After rotating the matrix will be {}".format(
        matrix
    ))
