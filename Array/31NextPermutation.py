"""A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [2,1, 3], [2,3,1],
[3,1,2], [3,2,1]. The next permutation of an array of integers is the next lexicographically greater permutation
of its integer. More formally, if all the permutations of the array are sorted in one container according to their
lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted
container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e.,
sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 100"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Steps I followed:
        1. Find the latest peak in the array (A peak is an element that is greater that the previous element in the array)
        2. If a peak is not found: it means it is in reverse order we just need to revert the array
        3. If a peak is found: it means we can rearrange the array and build a next permutation
        4. Iterate from the latest peak to the end of the array and find the min value in that subarray that is greater than the previous of the latest peak!
        This because we want to build the next greater permutation
        5. Swap the min value after the peak and the element previous the peak
        6. Sort the array from the latest_peak to the end of the array

        Time complexity = O(nlogn) - for sorted() function has TE O(NLogN)
        """

        latestPeak = False
        length = len(nums)

        for i in range(1, length):
            if nums[i - 1] < nums[i]:
                latestPeak = i

        if not latestPeak:
            nums.reverse()
            return

        pre_peak = latestPeak - 1
        min_after_peak = latestPeak
        for i in range(latestPeak, length):
            if nums[pre_peak] < nums[i] < nums[min_after_peak]:
                min_after_peak = i

        temp = nums[pre_peak]
        nums[pre_peak] = nums[min_after_peak]
        nums[min_after_peak] = temp

        nums[latestPeak:] = sorted(nums[latestPeak:])

        return


if __name__ == "__main__":
    nums = [1, 2, 3]
    nums1 = [1, 2, 3]
    Solution().nextPermutation(nums1)
    print("1. For given {} Int array. The next max Permutation is {}".format(
        nums, nums1
    ))


    nums = [3, 2, 1]
    nums1 = [3, 2, 1]
    Solution().nextPermutation(nums1)
    print("2. For given {} Int array. The next max Permutation is {}".format(
        nums, nums1
    ))

    nums = [3, 2, 1, 8, 9, 0]
    nums1 = [3, 2, 1, 8, 9, 0]
    Solution().nextPermutation(nums1)
    print("3. For given {} Int array. The next max Permutation is {}".format(
        nums, nums1
    ))