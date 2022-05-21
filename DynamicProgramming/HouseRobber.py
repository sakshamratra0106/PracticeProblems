# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Only its robbing the alternate houses
        evenRobSum = 0
        oddRobSum = 0
        for index, amount in enumerate(nums):
            if index % 2 == 0:
                evenRobSum += amount
            else:
                oddRobSum += amount

        return max(evenRobSum, oddRobSum)

    def rob1(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:

        TC : O(N)
        SC : O(1)
        """
        prevPrev = 0
        prev = 0
        for index in range(len(nums)):
            temp = prev
            prev = max(prevPrev + nums[index], prev)
            prevPrev = temp

        return prev
