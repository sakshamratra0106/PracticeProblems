# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/

class Solution:
    def climbStairs(self, n: int) -> int:

        # When we have to climb only upto two steps
        if n <= 2:
            return n

        # Three pointers
        prevPrev = 1
        prev = 2
        current = 0

        for i in range(3, n + 1):
            current = prevPrev + prev
            prevPrev, prev = prev, current

        return current
