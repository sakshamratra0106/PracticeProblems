from typing import List
from math import sqrt


class Solution:

    def __init__(self, board: List[List[int]]):
        self.board = board

    def isValidSudoku(self) -> bool:

        # Checking if it has a valid rows
        for row in self.board:
            # print(row)
            if self.isValidRow(row):
                continue
            else:
                return False

        # Checking if it has a valid Columns
        for i in range(len(self.board[0])):
            if self.isValidColumn(i):
                continue
            else:
                return False

        # Checking if it has a valid Sub Matrix of 3By3
        for i in range(int(sqrt(len(self.board)))):
            for j in range(int(sqrt(len(self.board)))):
                Matrix3By3 = [self.board[i * 3][j * 3: j * 3 + 3],
                              self.board[i * 3 + 1][j * 3: j * 3 + 3],
                              self.board[i * 3 + 2][j * 3: j * 3 + 3]]

                # print(Matrix3By3)
                if self.isValid3By3Matrix(Matrix3By3):
                    continue
                else:
                    return False

        return True

    def isValidRow(self, row: List[int]) -> bool:
        elements = {}
        for element in row:
            if element != "." and (9 < int(element)
                                   or int(element) < 1
                                   or element in elements):
                return False
            else:
                elements[element] = 1
        # print(elements)
        return True

    def isValidColumn(self, column: int):
        elements = {}
        for rowNum in range(len(self.board[0])):
            if self.board[rowNum][column] != "." and \
                    self.board[rowNum][column] in elements:
                # No need to check below condition as
                # This will be checked in isValidRow Function
                # or 9 < int(self.board[rowNum][column])
                # or int(self.board[rowNum][column]) < 1):
                elements[self.board[rowNum][column]] += 1
                return False
            else:
                elements[self.board[rowNum][column]] = 1
        # print(elements)
        return True

    def isValid3By3Matrix(self, matrix: List[List[int]]):
        elements = {}
        for row in matrix:
            for element in row:
                if element != "." and element in elements:
                    # or int(element) < 1
                    # or 9 < int(element)):
                    return False
                else:
                    elements[element] = 1

        # print(elements)
        return True

    # Better performance
    def isValidSudokuV2(self) -> bool:
        nums = {}
        for i in range(9):
            for j in range(9):
                if self.board[i][j] in nums.keys():
                    # if len(nums[board[i][j]]) ==9:
                    #     return False
                    for coord in nums[self.board[i][j]]:
                        if i == coord[0] or j == coord[1] or (i // 3 == coord[0] // 3 and j // 3 == coord[1] // 3):
                            return False
                    nums[self.board[i][j]].append([i, j])
                else:
                    if self.board[i][j] != '.':
                        nums[self.board[i][j]] = [[i, j]]
        return True


if __name__ == "__main__":
    board1 = [["5", "3", "7", ".", ".", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    board2 = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    # Driver this solution gives the time complexity as O(n2)
    sudoku1 = Solution(board1)
    print("Given sudoku is : {} \n and is this a Valid Sudoku True/False : {}"
          .format(board1, sudoku1.isValidSudoku()))

    sudoku2 = Solution(board2)
    print("Given sudoku is : {} \n and is this a Valid Sudoku True/False : {}"
          .format(board2, sudoku2.isValidSudoku()))

    # Better performing Code
    sudoku2 = Solution(board2)
    print("Given sudoku is : {} \n and is this a Valid Sudoku True/False : {}"
          .format(board2, sudoku2.isValidSudokuV2()))