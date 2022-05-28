# https://leetcode.com/problems/missing-number/

# https://leetcode.com/problems/missing-number/discuss/1091166/PythonGo-O(n)-by-math-w-Comment
from typing import List


class Solution:
    def missingNumber1(self, nums: List[int]) -> int:
        """
        TC : O(N**2)
        SC : O(1)
        """

        length = len(nums)

        if length == 0:
            return 0

        for index in range(length):

            if (index + 1) not in nums:
                return (index + 1)

        return 0

    def missingNumber(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:

        TC : O(N)
        SC : O(1)
        """
        # array containing n distinct numbers taken from 0, 1, 2, ..., n

        #   sum of ideal array without missing
        # = sum of array + missing element
        # = 0 + 1 + 2 + ... + missing element + ... + n
        # = 0 + 1 + 2 + ... + n
        # = 1 + 2 + ... + n
        # = (1+n)*n // 2
        #
        # => sum of ideal array without missing - sum of array = missing element

        n = len(nums)

        missing_element = (1 + n) * n // 2 - sum(nums)

        return missing_element