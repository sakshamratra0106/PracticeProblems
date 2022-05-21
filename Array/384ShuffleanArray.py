# https://leetcode.com/problems/shuffle-an-array/
# https://leetcode.com/problems/shuffle-an-array/solution/
from random import random

"""Initial Thoughts
Normally I would display more than two approaches, but shuffling is deceptively easy to do almost properly, 
and the Fisher-Yates algorithm is both the canonical solution and asymptotically optimal.

A few notes on randomness are necessary before beginning - both approaches displayed below assume that the languages
pseudorandom number generators (PRNGs) are sufficiently random. The sample code uses the simplest techniques available 
for getting pseudorandom numbers, but for each possible permutation of the array to be truly equally likely, 
more care must be taken. For example, an array of length nn has n!n! distinct permutations. Therefore, 
in order to encode all permutations in an integer space, \lceil lg(n!)\rceil⌈lg(n!)⌉ bits are necessary, 
which may not be guaranteed by the default PRNG."""


class Solution:
    """
    Complexity Analysis

    Time complexity : \mathcal{O}(n^2)O(n)
    The quadratic time complexity arises from the calls to list.remove (or list.pop), which run in linear time. nn linear list removals occur, which results in a fairly easy quadratic analysis.
    Space complexity : \mathcal{O}(n)O(n)
    Because the problem also asks us to implement reset, we must use linear additional space to store the original array. Otherwise, it would be lost upon the first call to shuffle.
    """
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        aux = list(self.array)

        for idx in range(len(self.array)):
            remove_idx = random.randrange(len(aux))
            self.array[idx] = aux.pop(remove_idx)

        return self.array


class SolutionV1:
    """
    Complexity Analysis
    Time complexity : \mathcal{O}(n)O(n)
    The Fisher-Yates algorithm runs in linear time, as generating a random index and swapping two values can be done in constant time.
    Space complexity : \mathcal{O}(n)O(n)
    Although we managed to avoid using linear space on the auxiliary array from the brute force approach, we still need it for reset, so we're stuck with linear space complexity.
    """
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
