# https://leetcode.com/problems/longest-common-subsequence/
# https://leetcode.com/problems/longest-common-subsequence/discuss/598687/Python-O(-m*n-)-2D-DP.-85%2B-w-Hint


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # padding one space for empty string representation
        text1 = ' ' + text1
        text2 = ' ' + text2

        w, h = len(text1), len(text2)

        dp_table = [[0 for x in range(w)] for y in range(h)]

        # update dynamic programming table with optimal substructure
        for y in range(1, h):
            for x in range(1, w):

                if text1[x] == text2[y]:
                    # with the same character
                    # extend the length of common subsequence
                    dp_table[y][x] = dp_table[y - 1][x - 1] + 1

                else:
                    # with different characters
                    # choose the optimal subsequence
                    dp_table[y][x] = max(dp_table[y - 1][x], dp_table[y][x - 1])

        return dp_table[-1][-1]


    # Implementation by top - down DP in python


    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:

        @cache
        def dp(i, j):

            if i == -1 or j == -1:
                # Any string compare to empty string has no common sequence
                return 0

            elif text1[i] == text2[j]:
                # Current character is the same
                return dp(i - 1, j - 1) + 1

            else:
                # Current characters are different
                return max(dp(i - 1, j), dp(i, j - 1))

        # -------------------------------------------------
        return dp(len(text1) - 1, len(text2) - 1)