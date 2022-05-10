# https://leetcode.com/problems/combination-sum-iii/
# https://leetcode.com/problems/combination-sum-iii/discuss/2024288/Python-andand-Recursion-andand-Backtracking
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        ans = []
        self.validCombination(k, n, ans, 1, [])

        return ans

    def validCombination(self, k, n, ans, i, intermediate):

        # when sum  and length is equal, we got our subset
        if k == len(intermediate) and n == sum(intermediate):
            # just take it into another ans array coz we are backtracking with i
            ans.append(intermediate)
            return

        # End Case
        if i == 10:
            return

        # take the element and check whether we can form a subset or not (s+[i] means storing it in list s).
        self.validCombination(k, n, ans, i + 1, intermediate + [i])
        # can we form a valid subset by not taking it
        self.validCombination(k, n, ans, i + 1, intermediate)
