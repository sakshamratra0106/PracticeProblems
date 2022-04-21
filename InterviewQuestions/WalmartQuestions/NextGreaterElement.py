from collections import deque
from typing import List


def next_greates_num(arry: List[int]):
    """

    :param arry:
    :return:

    TC : O(N^2)
    SC : O(N)
    """

    length = len(arry)
    next_greatest_element = []

    for index, element in enumerate(arry):

        j = index
        while j < length:
            if element < arry[j]:
                next_greatest_element.append(arry[j])
                break

            j += 1

        if j == length:
            next_greatest_element.append(-1)

    return next_greatest_element

# Find the next greater element for every element in a list
def findNextGreaterElements(input):
    """

    :param input:
    :return:

    TC : O(N)
    SC : O(N)
    """
    # base case
    if not input:
        return

    result = [-1] * len(input)

    # create an empty stack
    s = deque()

    # do for each element
    for i in range(len(input)):

        # loop till we have a greater element on top or stack becomes empty.

        # Keep popping elements from the stack smaller than the current
        # element, and set their next greater element to the current element
        while s and input[s[-1]] < input[i]:
            result[s[-1]] = input[i]
            s.pop()

        # push current "index" into the stack
        s.append(i)
        # print(result,"--",s)

    return result


if __name__ == '__main__':
    input = [2, 7, 3, 5, 4, 6, 8]
    print(findNextGreaterElements(input))
    input = [2, 7, 3, 5, 4, 6, 8]
    print(next_greates_num(input))
