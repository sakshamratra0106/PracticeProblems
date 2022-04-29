# https://leetcode.com/problems/first-bad-version/


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(i):
    # Implimentated as an API in leetcode problem
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """

        :param n:
        :return:
        TC : O(N)

        """
        for i in range(n):
            if isBadVersion(i):
                return i

        return n

    def firstBadVersion1(self, n: int) -> int:
        """

        :param n:
        :return:

        TC : O(Log N)
        """
        left = 1
        right = n
        while left < right:

            # left+(right-left)/2 instead of (left+right)/2 to prevent overflow

            mid = left + int((right - left) / 2)

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

