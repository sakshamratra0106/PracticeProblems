from typing import List


class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Timed Out Code
        # TC : O(N^2)
        length = len(nums)
        count = 0
        while count < k:
            temp = nums[length - 1]
            index = length - 1
            for index in range(length - 1, 0, -1):
                nums[index] = nums[index - 1]
                index -= 1

            nums[0] = temp
            count += 1

    def rotate2(self, nums: List[int], k: int) -> None:
        """

        :param nums:
        :param k:
        :return:

        code is not working
        """
        # Not Working
        length = len(nums)
        elementRecord = {}
        for index,element in enumerate(nums):
            elementRecord[index] = element

        for index, element in enumerate(nums):

            if (index + k) / length < 0:
                nums[index] = elementRecord[index + k]
            else:
                nums[index] = elementRecord[((index + k) % length)]

    def rotate3(self, nums: List[int], k: int) -> None:
        """

        :param nums:
        :param k:
        :return:


        """
        # TC : O(N)
        # SC : O(1)

        length = len(nums)
        if length == 0 or length <= 0:
            return

        if k > length:
            while k > length:
                k -= length

        nums.reverse()

        def reverse(left, right, nums):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return nums

        nums = reverse(0, k - 1, nums)
        nums = reverse(k, length - 1, nums)

        return


if __name__ == "__main__":

    nums = [1,2,3,4,5,6,7]
    nums1 = [1,2,3,4,5,6,7]
    k = 3
    Solution().rotate1(nums1, k)
    print("1. for a given array {} after rotating for {} steps array will be {}".format(
        nums, k, nums1
    ))

    nums = [-1,-100,3,99]
    nums1 = [-1,-100,3,99]
    k = 2
    Solution().rotate2(nums1, k)
    print("2. for a given array {} after rotating for {} steps array will be {}".format(
        nums, k, nums1
    ))