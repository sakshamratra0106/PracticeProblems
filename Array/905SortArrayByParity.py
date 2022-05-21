from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        TC : O(N)
        SC : O(1)
        """
        length = len(nums)
        evenIndex = 0
        oddIndex = length - 1

        while evenIndex < oddIndex:

            # Find next index where we have an odd number
            # Condition for Overflow of index
            while evenIndex < length and nums[evenIndex] % 2 == 0:
                evenIndex += 1

            # Find next index where we have an even number
            # Condition for underflow of index
            while oddIndex > -1 and nums[oddIndex] % 2 != 0:
                oddIndex -= 1

            # Swap both index in place
            if evenIndex < oddIndex:
                nums[evenIndex], nums[oddIndex] = nums[oddIndex], nums[evenIndex]
                evenIndex += 1
                oddIndex -= 1

        return nums

    def sortArrayByParity1(self, nums: List[int]) -> List[int]:
        """
        TC : O(N)
        SC : O(1)
        """
        even, odd = 0 , len(nums) - 1 #2 pointers to keep a track of even and odd numbers
        while even <= odd:
            if nums[even] % 2 != 0: # if we have odd numbers at the beginning , swap and move them to end of list
                nums[even],nums[odd] = nums[odd],nums[even]
                odd -= 1
            elif nums[odd] % 2 == 0: # if we have even numbers at the end , swap and move them to beginning of list
                nums[even],nums[odd] = nums[odd],nums[even]
                even += 1
            else: #if the parity is as required (even integers at the beginning, odd at the end) - check next
                odd -= 1
                even += 1

            print(nums)

        return nums
