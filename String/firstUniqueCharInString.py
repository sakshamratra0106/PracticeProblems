import collections


class Solution:
    def __init__(self, s: str):
        self.string = s

    def firstUniqChar(self) -> int:
        charSet = {}
        for e in self.string:
            if e in charSet:
                charSet[e] += 1
            else:
                charSet[e] = 1

        for index in range(len(self.string)):
            if self.string[index] in charSet \
                    and charSet[self.string[index]] == 1:
                return index
        return -1

    def firstUniqCharLeetCodeSolution(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """

        # Complexity Analysis
        #
        #     Time complexity : \mathcal{O}(N)O(N) since we go through the string of length N two times.
        #     Space complexity : \mathcal{O}(1)O(1) because English alphabet contains 26 letters.

        # build hash map : character and how often it appears
        count = collections.Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


if __name__ == "__main__":
    # Getting the first unique character
    # in O(n)

    string1 = "loveleetcode"
    print("First Unique Character in the string {} is at index {}"
          .format(string1, Solution(string1).firstUniqChar() + 1))

    string1 = "aabb"
    print("First Unique Character in the string {} is at index {}"
          .format(string1, Solution(string1).firstUniqChar() + 1))

    string1 = ""
    print("First Unique Character in the string {} is at index {}"
          .format(string1, Solution(string1).firstUniqChar() + 1))