# https://www.code-recipe.com/post/two-sum


# Often, when dealing with iterators, we also get a need to keep a count of iterations.
# Python eases the programmers’
# task by providing a built-in function enumerate() for this task.

# Whereas brute force with two loops it will take time complexity to O(n^2)
from typing import List


def sumOfTwoNumbers(nums: List[int], target: int):
    """

    :param nums:
    :param target:
    :return:

    # Time Complexity: O(n)
    #
    # Space Complexity: O(n)
    """
    seen = {}
    for i, element in enumerate(nums):
        difference = target - element
        if difference in seen:
            return seen[difference], i

        seen[element] = i


def sumOfTwoNumbers1(nums: List[int], target: int):
    """
    
    :param nums: 
    :param target: 
    :return: 
    
    # Return the index of two nums == target
    # Given input list is sorted
    
    # Time Complexity O(N)
    # Space Complexity O(1)
    """""

    # if list is empty
    if nums is None:
        return [-1, -1]

    start = 0
    end = len(nums) - 1
    while start < end:
        if nums[start] + nums[end] == target:
            return [start, end]
        elif nums[start] + nums[end] < target:
            start += 1
        else:
            end -= 1
    # If sum of two == target not found
    return [-1, -1]


if __name__ == '__main__':
    # Driver Program
    arr2 = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
    print("1. In Array", arr2, " Sum of 10 is available at index", sumOfTwoNumbers(arr2, -10))

    # If the input is sorted
    arr2 = [-93, -53, -41, -23, 26, 31, 58, 59, 84, 97, ]
    print("2. In Array", arr2, " Sum of 10 is available at index", sumOfTwoNumbers1(arr2, -10))