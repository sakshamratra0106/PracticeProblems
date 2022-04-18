"""
Question : https://leetcode.com/problems/last-stone-weight/

Data Structure - Heap Implementation
Unfortunately, due to the implementation of the list data structure, even the binary search optimisation cannot break free of the O(n) insert.
If only there was a data structure that could help us sort and insert automatically without having to rely on a heavier insert function...

Python has an in-built heap library that is perfect for this task.
Essentially, all we need to do is insert the elements, and the heap will settle the sorting order for us.
Unfortunately, Python's heap library implements a min-heap instead of a max-heap, whereby popping will give us the lightest stone instead of the heaviest stone.

A standard (very common!) workaround is to negate all the weight values of the stones.
This way, the heaviest stone has the most negative value, and hence becomes the smallest value in the heap.
Then, all we have to do after obtaining the value from the heap is to un-negate the value to use it in our calculations.


TC: O(nlogn); heappush() and heappop() both have O(logn) time complexity, and are both nested in the while loop.
    Note: heapify() runs in O(n) time, hence the time complexity is not affected.
SC: O(1); both the negation and the heapify are done in-place.
"""
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        TC : O(N^2)
        SC : O(1)
        """

        length = len(stones)

        if length == 0:
            return 0
        elif length == 1:
            stones[0]

        stones.sort(reverse=True)
        # print(stones)

        while length > 1:
            difference = stones[0] - stones[1]
            stones[:] = stones[2:]
            if difference == 0:
                length -= 1
            else:
                stones.insert(0, difference)
            stones.sort(reverse=True)
            length -= 1
            # print(stones)

        if len(stones) == 0:
            return 0

        return stones[0]

    def lastStoneWeight1(self, stones: List[int]) -> int:

        # first, negate all weight values in-place
        for i, s in enumerate(stones):
            stones[i] = -s

        heapify(stones)  # pass all negated values into the min-heap

        while stones:
            s1 = -heappop(stones)  # the heaviest stone
            if not stones:  # s1 is the remaining stone
                return s1
            s2 = -heappop(stones)  # the second-heaviest stone; s2 <= s1
            if s1 > s2:
                heappush(stones, s2 - s1)  # push the NEGATED value of s1-s2; i.e., s2-s1
            # else s1 == s2; both stones are destroyed
        return 0  # if no more stones remain


if __name__ == "__main__":
    stoneWeigths = [2, 7, 4, 1, 8, 1]
    print("1. Last stone weight will be : {}".format(
        Solution().lastStoneWeight(stoneWeigths)
    ))

    stoneWeigths = [2, 7, 4, 1, 8, 1]
    print("2. Last stone weight will be : {}".format(
        Solution().lastStoneWeight1(stoneWeigths)
    ))

    stoneWeigths = [2, 9]
    print("3. Last stone weight will be : {}".format(
        Solution().lastStoneWeight1(stoneWeigths)
    ))