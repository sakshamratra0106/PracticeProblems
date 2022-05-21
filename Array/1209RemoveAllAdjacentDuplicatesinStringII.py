# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/discuss/2012031/Python-Stack-Solution-with-Explanation
from collections import deque


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque()  # list works fine too
        for ch in s:
            if stack and stack[-1][0] == ch:  # current character belongs to the previous substring
                stack[-1][1] += 1
                if stack[-1][1] == k:  # k-length substring reached, remove substring
                    _ = stack.pop()
            else:  # current character is its own substring
                stack.append([ch, 1])
        return ''.join(ch * n for ch, n in stack)  # concatenate remaining substrings
