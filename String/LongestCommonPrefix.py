from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """

        :param strs: List of strings
        :return: Longest Common Prefix

        This function does the calculation in
        O(N^2) time complexity and O(1) Space complexity

        ## Leetcode Solutions
        https://leetcode.com/problems/longest-common-prefix/solution/

        """

        # If the first string is "" return ""
        if strs[0]:
            shortestString = strs[0]
        else:
            return ""

        # Find the shortest string
        # that could be the longest common prefix
        for str in strs:
            if len(str) < len(shortestString):
                shortestString = str

        # print(shortestString)

        # Finding Common longest prefix
        # O(N^2) time complexity and O(N) Space complexity
        commonPrefix = ""
        for innerIndex in range(len(shortestString)):
            for outerIndex in range(1, len(strs)):
                if strs[outerIndex - 1][innerIndex] != strs[outerIndex][innerIndex]:
                    return commonPrefix
            commonPrefix += (strs[0][innerIndex])

        return commonPrefix


if __name__ == "__main__":

    strs = ["flower", "flow", "flight"]
    print("1. Given an array of Strings : {}. Common longest common prefix would be : \"{}\"".format(
        strs, Solution().longestCommonPrefix(strs)
    ))

    strs = ["dog","racecar","car"]
    print("2. Given an array of Strings : {}. Common longest common prefix would be : \"{}\"".format(
        strs, Solution().longestCommonPrefix(strs)
    ))