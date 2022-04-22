from typing import List


def sumEqualsTarget(array : List[int], target: int) -> List[int]:
    """

    :param array:
    :param target:
    :return:

    TC : O(N)
    SC : O(N)

    Input can be unsorted
    """
    difference = {}
    for index, ele in enumerate(array):
        diff = target - ele
        if diff in difference:
            return [index, difference[diff]]
        else :
            difference[ele] = index

    return [-1, -1]


def sumEqualsTarget1(array: List[int], target: int) -> List[int]:
    """

    :param array:
    :param target:
    :return:

    TC : O(N)
    SC : O(1)

    Two Pointers solution only when input is in sorted order.
    """

    length = len(array)
    start = 0
    end = length - 1
    while start < end:
        if array[start] + array[end] == target:
            return [start, end]
        elif array[start] + array[end] < target:
            start += 1
        else:
            end -= 1

    return [-1, -1]

