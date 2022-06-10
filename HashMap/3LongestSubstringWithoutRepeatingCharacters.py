# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/2132791/Python-Easy-2-approaches
from collections import defaultdict


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        """This approach uses counter variable to track number of characters in a sliding window.
        Whenever we encounter a state where the window becomes invalid due to number of characters(count of any character > 1),
        we would update the left bound of the new valid window.

        Time - O(2n) - Iterates both l and r once through the input s.
        Space - O(n)"""

        counter = defaultdict(int)  # track counts of each character
        l = 0
        max_length = 0
        for r, c in enumerate(s):
            counter[c] += 1
            if counter[c] > 1:
                while l < r and counter[c] > 1:  # iterate until window is valid
                    counter[s[l]] -= 1
                    l += 1
            max_length = max(max_length, r - l + 1)
        return max_length

    def lengthOfLongestSubstring1(self, s: str) -> int:
        """

        If we observe the previous approach, we would notice we don't need to track the counts of each character in a sliding window.
        We just need to track the last seen of a character.
        This will help us figure out whether a character exists in the current sliding window.



        Time - O(n) - Iterates both l and r once through the input s.
        Space - O(n)
        """

        last_seen = {}
        left = 0
        maxGlobalLength = 0

        for index, element in enumerate(s):

            if element in last_seen:
                left = max(last_seen[element], left)

            last_seen[element] = index + 1
            maxGlobalLength = max(maxGlobalLength, index + 1 - left)

            # Debuging
            # print(last_seen, maxGlobalLength, index + 1 - left)

        return maxGlobalLength


