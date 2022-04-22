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

    def returnDuplicates(self, nums: List[int]) -> List[int]:
        """

        :param nums:
        :return:

        Time Complexity is O(N)
        Space Complexity is O(N)

        """
        unique = {}
        for index, element in enumerate(nums):
            if element in unique:
                unique[element] += 1
            else:
                unique[element] = 1

        return [element for element in unique if unique[element] > 1]

    def returnDuplicates1(self, nums: List[int]) -> List[int]:
        """

        :param nums:
        :return:

        Time Complexity is O(N)
        Space Complexity is O(1)

        Approach: The basic idea is to use a HashMap to solve the problem. But there is a catch,
        the numbers in the array are from 0 to n-1, and the input array has length n.
        So, the input array can be used as a HashMap. While Traversing the array, if an element ‘a’ is encountered
        then increase the value of a%n‘th element by n.
        The frequency can be retrieved by dividing the a % n’th element by n.

        For reference
        https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
        """

        length = len(nums)
        for index in range(length):
            val = nums[index] % length
            nums[val] = nums[val] + length

        print("Printing Duplicate values")
        for i in range(length):
            if nums[i] >= length * 2:
                print(i, end=" ")
        print()
        return


if __name__ == "__main__":
    nums = [1, 1, 2]
    print("1. Given a sorted array : {}. Updated array with unique elements till index is : {}.".format(
        nums, Solution().removeDuplicates(nums)
    ))

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print("2. Given a sorted array : {}. Updated array with unique elements till index is : {}.".format(
        nums, Solution().removeDuplicates(nums)
    ))

    # Return duplicates

    # O(N) and O(N)
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print("3. Given a sorted array : {}. Updated array with unique elements till index is : {}.".format(
        nums, Solution().returnDuplicates(nums)
    ))

    # O(N) and O(1)
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5]
    print("4. Given a sorted array : {}. Updated array with unique elements till index is : {}.".format(
        nums, Solution().returnDuplicates1(nums)
    ))