from typing import List


class GeneratePascalsTriangle:

    def __init__(self, numRows: int):
        self.numRows = numRows

    def generateN3(self) -> List[List[int]]:
        # Python 3 code for Pascal's Triangle
        # A simple O(n^3)
        # program for
        # Pascal's Triangle

        for line in range(0, self.numRows):

            # Every line has number of
            # integers equal to line
            # number
            for i in range(0, line + 1):
                print(self.binomialCoeff(line, i),
                      " ", end="")
            print()

    # See https://www.geeksforgeeks.org/space-and-time-efficient-binomial-coefficient/
    # for details of this function
    def binomialCoeff(self, n, k):
        res = 1
        if k > n - k:
            k = n - k
        for i in range(0, k):
            res = res * (n - i)
            res = res // (i + 1)

        return res

    def generateN2(self) -> List[List[int]]:

        # Time complexity is On2 and space complexity is On2
        # A O(n^2) time and O(n^2) extra
        # space method for Pascal's Triangle

        if self.numRows <= 0:
            return []
        elif self.numRows == 1:
            return [[1]]
        elif self.numRows == 2:
            return [[1], [1, 1]]
        else:
            pascalsTriangle = [[1], [1, 1]]
            for row in range(2, self.numRows):
                pascalsTriangle.append([])
                for element in range(row + 1):
                    if element - 1 < 0:
                        topLeft = 0
                    else:
                        topLeft = pascalsTriangle[row - 1][element - 1]

                    if row == element:
                        topRight = 0
                    else:
                        topRight = pascalsTriangle[row - 1][element]
                    # print("row : {} element : {} topLeft : {} topRight : {} pascalElement : {}"
                    #       .format(row,element,topLeft,topRight,topLeft+topRight))
                    pascalsTriangle[row].append(topLeft + topRight)
            return pascalsTriangle

    def generateN2M1(self) -> List[List[int]]:

        # Time complexity is On2 and space complexity is On2
        # A O(n^2) time and O(1) extra
        # space method for Pascal's Triangle
        # Method 3 ( O(n^2) time and O(1) extra space )
        # This method is based on method 1. We know that ith entry in a line number line is Binomial Coefficient C(line, i) and all lines start with value 1. The idea is to calculate C(line, i) using C(line, i-1). It can be calculated in O(1) time using the following.
        #
        #
        # C(line, i)   = line! / ( (line-i)! * i! )
        # C(line, i-1) = line! / ( (line - i + 1)! * (i-1)! )
        # We can derive following expression from above two expressions.
        # C(line, i) = C(line, i-1) * (line - i + 1) / i
        #
        # So C(line, i) can be calculated from C(line, i-1) in O(1) time

        for line in range(1, self.numRows + 1):
            C = 1;  # used to represent C(line, i)
            for i in range(1, line + 1):
                # The first value in a
                # line is always 1
                print(C, end=" ");
                C = int(C * (line - i) / i);
            print("");


if __name__ == "__main__":
    print("Generating Pascals Triangle with -6 number of rows is {}"
          .format(GeneratePascalsTriangle(-6).generateN2()))
    print("Generating Pascals Triangle with 0 number of rows is {}"
          .format(GeneratePascalsTriangle(0).generateN2()))
    print("Generating Pascals Triangle with 1 number of rows is {}"
          .format(GeneratePascalsTriangle(1).generateN2()))
    print("Generating Pascals Triangle with 2 number of rows is {}"
          .format(GeneratePascalsTriangle(2).generateN2()))
    print("Generating Pascals Triangle with 3 number of rows is {}"
          .format(GeneratePascalsTriangle(3).generateN2()))
    print("Generating Pascals Triangle with 4 number of rows is {}"
          .format(GeneratePascalsTriangle(4).generateN2()))
    print("Generating Pascals Triangle with 10 number of rows is {}"
          .format(GeneratePascalsTriangle(10).generateN2()))

    print("Generating Pascals Triangle with N3 using  Binomial Coefficient")

    print("Generating Pascals Triangle with 10 number of rows is {}"
          .format(GeneratePascalsTriangle(10).generateN3()))
    print("Generating Pascals Triangle with 11 number of rows is {}"
          .format(GeneratePascalsTriangle(11).generateN3()))

    print("Generating Pascals Triangle with N2 and M1 using  Binomial Coefficient")

    print("Generating Pascals Triangle with 10 number of rows is {}"
          .format(GeneratePascalsTriangle(10).generateN2M1()))
    print("Generating Pascals Triangle with 11 number of rows is {}"
          .format(GeneratePascalsTriangle(11).generateN2M1()))
