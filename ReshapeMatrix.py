from typing import List


class Matrix:

    def __init__(self, inputMatrix: List[List[int]]):
        self.matrix = inputMatrix

    def returnMatrix(self) -> List[List[int]]:
        return self.matrix

    #### TO DO ####
    def showMatrix(self) -> None:
        for row in self.matrix:
            for element in row:
                print(element, end=" ")
            print()

    def reshapeMatrix(self, r: int, c: int) -> List[List[int]]:

        # Its time complexity is O(r * c)

        availableRows = len(self.matrix)

        if availableRows > 0:
            availableColumns = len(self.matrix[0])
        else:
            return []

        # print(availableColumns * availableRows, "--", r * c)

        if availableColumns * availableRows != r * c:
            return self.matrix

        OneDMatrix = []
        for row in self.matrix:
            for element in row:
                OneDMatrix.append(element)

        reshapedMatrix = [[0 for row in range(c)] for element in range(r)]
        k = 0
        for row in range(r):
            for column in range(c):
                reshapedMatrix[row][column] = OneDMatrix[k]
                k += 1

        return reshapedMatrix


if __name__ == "__main__":
    # DriverCode
    matrix = Matrix([[1, 2], [3, 4]])
    print("Reshaping given matrix input by rows {} and columns {}. "
          "Given Input Matrix is : {} \n "
          "Reshaped matrix is {}"
          .format(2, 4, matrix.returnMatrix(), matrix.reshapeMatrix(2, 4)))

    print("Reshaping given matrix input by rows {} and columns {}. "
          "Given Input Matrix is : {} \n "
          "Reshaped matrix is {}"
          .format(1, 4, matrix.returnMatrix(), matrix.reshapeMatrix(1, 4)))
