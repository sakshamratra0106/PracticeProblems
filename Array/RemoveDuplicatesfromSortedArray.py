from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        """

        :param nums:
        :return:

        Two Pointers Method
        time complexity O(N) and O(1)
        Given when array is sorted
        """

        # Base Case. Return o when list is empty
        if nums is None:
            return 0

        # Two Pointer and previous value
        uniqueIndex = 0
        previous = nums[0]
        current = 1

        # Loop through
        # Update unique index when previous is not equal to the current
        for i in range(1, len(nums)):

            if previous == nums[current]:
                previous = nums[current]
                current += 1
            else:
                uniqueIndex += 1
                nums[uniqueIndex] = nums[current]
                previous = nums[current]
                current += 1

            # Will through index out of range error when run with print. Make range len -1. then run to debug
            # That will not process only last element
            # print(i, "--", previous, "--", nums[current], "--", uniqueIndex, "--", nums[uniqueIndex])

        return uniqueIndex + 1


if __name__ == "__main__":
    nums = [1, 1, 2]
    print("1. Given a sorted array : {}. Updated array with unique elements till index is : {}.".format(
        nums, Solution().removeDuplicates(nums)
    ))

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print("2. Given a sorted array : {}. Updated array with unique elements till index is : {}.".format(
        nums, Solution().removeDuplicates(nums)
    ))
