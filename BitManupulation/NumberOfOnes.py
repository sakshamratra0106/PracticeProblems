# https://leetcode.com/problems/number-of-1-bits
# https://leetcode.com/problems/number-of-1-bits/discuss/1694753/Python-solution(kernighans-algorithm)
#
# Let's take example of number 5
# binary representation of 5 is 101
# so it's rightmost bit mask would be 001
# how we get it?
# rsbm = n & (n's 2's complement)
# rsbm = n & (~n+1)
# n = n-rsbm so now our number is 100
# we will loop it until number is 000
# simple!
# below is python implementation :


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            last_bit = n & (~n + 1)
            n = n - last_bit
            count += 1

        return count