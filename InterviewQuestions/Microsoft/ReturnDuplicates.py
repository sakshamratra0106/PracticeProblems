# 2. Return duplicate values in an array where value can not be out size the range (0,n-1)
#
# arry = [] -> n
# contrainrs = (0,n-1)
#
# 	1. n*2 , 1 - Solved
# 	2. n , n - Solved
# 	3. n and 1 - ?
#
# [1,2,3,6,3,6,1]
#
# return [duplicate element]
from typing import List


def returnDuplicates(array: List[int]):
    """

    :param array:
    :return:

    TC : O(N)
    SC : O(N)
    """
    unique = set()
    duplicates = []
    for ele in array:
        if ele in unique:
            duplicates.append(ele)
        else:
            unique.add(ele)
    return duplicates


def returnDuplicates1(array: List[int]):
    """

    :param array:
    :return:

    TC : O(N)
    SC : O(1)

    Given array where value can not be out size the range (0,n-1)
    Returns elements which were having least one duplicates
    """

    length = len(array)
    for index, ele in enumerate(array):
        val = ele % length
        array[val] = array[val] + length

    for index, ele in enumerate(array):
        if ele // length >= 2:
            print(index, end=" ")
    print()


if __name__ == "__main__":
    array = [1, 2, 3, 6, 3, 6, 1]
    print("For a given array {}. List of duplicates will be {}".format(
        array, returnDuplicates(array)
    ))
    array = [1, 2, 3, 6, 3, 6, 1]
    print("For a given array {}. List of duplicates will be {}".format(
        array, returnDuplicates1(array)
    ))
