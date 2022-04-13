# https://leetcode.com/problems/spiral-matrix-ii/
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        left = top = 0
        right = bottom = n - 1
        k = 1

        while k <= n * n:
            for c in range(left, right + 1):
                res[top][c] = k
                k += 1
            for r in range(top + 1, bottom + 1):
                res[r][right] = k
                k += 1
            for c in range(right - 1, left - 1, -1):
                res[bottom][c] = k
                k += 1
            for r in range(bottom - 1, top, -1):
                res[r][left] = k
                k += 1

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return res
