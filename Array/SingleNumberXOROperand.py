from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:

        TC : O(N)
        SC : O(1)

        """

        length = len(nums)

        if length == 0:
            return None
        elif length == 1:
            return nums[0]

        num = nums[0]

        # Iterate through using XOR operator
        # to find a number which appeared only once
        for i in range(1, length):
            num ^= nums[i]

        return num


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    print("1. For a given array {} the number which appeared only once is {}".format(
        nums, Solution().singleNumber(nums)
    ))

    nums = [2, 2, 1]
    print("2. For a given array {} the number which appeared only once is {}".format(
        nums, Solution().singleNumber(nums)
    ))
