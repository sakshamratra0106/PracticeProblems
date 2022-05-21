"""You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i].
You can divide each pile into any number of sub piles, but you cannot merge two piles together.

You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies.
Each child can take at most one pile of candies and some piles of candies may go unused.

Return the maximum number of candies each child can get.

Example 1:

Input: candies = [5,8,6], k = 3
Output: 5
Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1.
We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children.
It can be proven that each child cannot receive more than 5 candies.

Input: candies = [2,5], k = 11
Output: 0
Explanation: There are 11 children but only 7 candies in total, so it is impossible to ensure each child receives at least one candy.
Thus, each child gets no candy and the answer is 0.

Constraints:

1 <= candies.length <= 105
1 <= candies[i] <= 107
1 <= k <= 1012"""

from typing import List


class Solution:

    def canSplit(self, candies, numCandies, k):
        """

        :param numCandies:
        :param candies:
        :param k:
        :return:

        Iterate through the Candies to check if can there be numCandies of  candies for k kids
        """
        split = 0
        for i in candies:
            split += i // numCandies
        if split >= k:
            return True
        else:
            return False

    def maximumCandies(self, candies: List[int], k: int) -> int:
        """

        :param candies:
        :param k:
        :return:

        This does a binary search from 1 to sum of total candies to check
        which number is max num of candies
        TC : O(LogN)
        SC : O(1)
        """
        end = sum(candies)
        start = 1
        ans = 0
        while start <= end:
            mid = (start + end) // 2
            if self.canSplit(candies, mid, k):
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans


if __name__ == "__main__":
    candies = [2, 5]
    k = 11
    print("Given Candies {} can be divided in between {} kids equally if given {} to each.".format(
        candies, k, Solution().maximumCandies(candies, k)
    ))

    candies = [5, 8, 6]
    k = 3
    print("Given Candies {} can be divided in between {} kids equally if given {} to each.".format(
        candies, k, Solution().maximumCandies(candies, k)
    ))
