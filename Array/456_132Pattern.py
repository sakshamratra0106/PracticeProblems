# https://leetcode.com/problems/132-pattern/
# https://leetcode.com/problems/132-pattern/discuss/2015560/Python3-monotonic-stack-with-detailed-explanation-time%3A-O(n)-space%3A-O(n)
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        TC : O(N)
        SC : O(N)

        :param nums:
        :return:
        """
        s3 = float('-inf')
        s3_candidates = []

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < s3:
                return True
            # When s3 is not -inf, meaning we have a valid s2, s3 pair. We first let nums[i]
            # act as s1, the smallest number among the three. If nums[i] is smaller than s3,
            # we find a 132 pattern and return True.

            while s3_candidates and nums[i] > s3_candidates[-1]:
                s3 = s3_candidates.pop()
                # Else, we assume that nums[i] now is s2 for the next iteraton. If numbers
                # in s3_candidates is smaller than nums[i], we find a valid s2, s3 pair.
            s3_candidates.append(nums[i])
            # Additionally, this while loop removes all numbers in stack that smaller than
            # nums[i], then push nums[i] into the stack, making sure that the stack keeps a
            # deceasing order. Therefore, the last popped num from this stack will always be
            # the maximun s3 and will not miss possible s1.
        return False