from typing import List


class Solution:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def searchMatrixN2(self,
                       target: int) -> bool:

        # Searching a Target in a Matrix
        # with time complexity N2 and Memory as 1
        for row in self.matrix:
            for element in row:
                if element == target:
                    return True

        return False

    def binarySearch(self, arr: List[int], beginFromIndex: int, endIndex: int, target: int) -> bool:

        if endIndex >= beginFromIndex:

            mid = beginFromIndex + (endIndex - beginFromIndex) // 2

            if arr[mid] == target:
                return mid

            # if target is < then mid element
            # search in the first half of the array
            elif arr[mid] > target:
                return self.binarySearch(arr, beginFromIndex, mid - 1, target)

            # if target is > then mid element
            # search in second half
            else:
                return self.binarySearch(arr, mid + 1, endIndex, target)


        # Incase array is of zero length
        else:
            return -1

    def searchMatrixNLogN(self,
                          target: int) -> bool:

        # Searching a Target in a Matrix
        # with time complexity O(N * LogN) and Memory as 1
        for row in self.matrix:
            if self.binarySearch(row, 0, len(row) - 1, target) >= 0:
                return True

        return False


if __name__ == "__main__":
    # Matrix Search with
    # time complexity O(N^2)
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print("Matrix {} has Target {} in it ? {}".format(
        matrix, target, Solution(matrix).searchMatrixN2(target)
    ))

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    print("Matrix {} has Target {} in it ? {}".format(
        matrix, target, Solution(matrix).searchMatrixN2(target)
    ))

    # Binary Search
    # Time complexity O(log n)
    array = [1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
    target = 16
    print("Array {} has Target {} in it ? if yes is at index {}".format(
        array, target, Solution(None).binarySearch(array, 0, len(array) - 1, target)
    ))

    array = [1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
    target = 90
    print("Array {} has Target {} in it ? if yes is at index {}".format(
        array, target, Solution(None).binarySearch(array, 0, len(array) - 1, target)
    ))

    # Matrix Search with
    # time complexity O(N * Log N)
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print("Matrix {} has Target {} in it ? {}".format(
        matrix, target, Solution(matrix).searchMatrixNLogN(target)
    ))

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    print("Matrix {} has Target {} in it ? {}".format(
        matrix, target, Solution(matrix).searchMatrixNLogN(target)
    ))
