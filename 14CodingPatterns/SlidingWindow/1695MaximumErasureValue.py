# https://leetcode.com/problems/maximum-erasure-value/
from typing import List


class Solution:
    def maximumUniqueSubarray1(self, nums: List[int]) -> int:
        """

        current sliding window
        Intuition
        Error : TLE

        Time - O(n*2)
        Space - O(n)
        """

        last_seen = {}
        left = 0
        # maxGlobalLength = 0
        maxSum = 0
        currentSum = 0

        for index, element in enumerate(nums):

            if element in last_seen:
                left = max(last_seen[element], left)
                currentSum = sum(nums[left: index])

            last_seen[element] = index + 1
            currentSum = currentSum + element
            # maxGlobalLength = max(maxGlobalLength, index - left + 1)
            maxSum = max(maxSum, currentSum)

            # Debuging
            # print(last_seen, maxGlobalLength, index + 1 - left)

        return maxSum

    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        TC : O(N)
        TC : O(K) .. number of unique elements

        """
        seen = set()
        max_sum, curr_sum, l = 0, 0, 0

        for num in nums:

            while num in seen:
                curr_sum -= nums[l]
                seen.remove(nums[l])
                l += 1

            curr_sum += num
            seen.add(num)
            max_sum = max(curr_sum, max_sum)

        return max_sum