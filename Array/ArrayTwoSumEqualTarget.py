# https://www.code-recipe.com/post/two-sum


# Often, when dealing with iterators, we also get a need to keep a count of iterations. Python eases the programmers’ task by providing a built-in function enumerate() for this task.
# Time Complexity: O(n)
#
# Space Complexity: O(n)
# Where as brute force with two loops it will take time complexity to O(n^2)
from typing import List


def sumOfTwoNumbers(nums : List[int], target: int):
    seen={}
    for i,element in enumerate(nums):
        difference = target - element
        if difference in seen:
            return seen[difference], i

        seen[element]=i


if __name__ == '__main__':

    #Driver Program
    arr2 = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

    print("In Array",arr2," Sum of 10 is available at index",sumOfTwoNumbers(arr2,-10))