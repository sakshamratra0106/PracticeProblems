from typing import List

"""You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
 
Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """

        :param height:
        :return:

        Calculates the Max Rain water trapped

        TC : O(N)
        SC : O(1)
        Two Pointers, Greedy Method

        """

        width = len(height)

        if width == 0 or width == 1:
            return 0

        maxArea = 0
        leftSide = 0
        rightSide = width - 1

        while leftSide < rightSide:
            maxArea = max(maxArea, (rightSide - leftSide) * min(height[leftSide], height[rightSide]))

            if height[leftSide] < height[rightSide]:
                leftSide += 1
            else:
                rightSide -= 1

        return maxArea


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("1. Max rain water that can be trapped by given heights {} will be {}.".format(
        height, Solution().maxArea(height)
    ))

    height = [1,1]
    print("2. Max rain water that can be trapped by given heights {} will be {}.".format(
        height, Solution().maxArea(height)
    ))