from math import gcd
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        if (k := k%(m*n)) == 0:  # after k shifts, final array = grid
            return grid
        div = gcd(m*n, k)  # math.gcd
        for i in range(div):
            r, c = divmod(i, n)
            curr = grid[r][c]  # obtain initial element
            for j in range(m*n//div):
                r, c = divmod((i+k*(j+1))%(m*n), n)  # get the resultant index
                grid[r][c], curr = curr, grid[r][c]  # perform swap operation
        return grid