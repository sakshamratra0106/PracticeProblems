# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Solutions
# https://www.tutorialspoint.com/letter-combinations-of-a-phone-number-in-python
# https://www.geeksforgeeks.org/iterative-letter-combinations-of-a-phone-number/
from collections import deque
from typing import List


class Solution(object):
    def letterCombinations(self, digits):
        """

        Recursive Way Of Doing it.

        :param digits:
        :return:
        """
        if len(digits) == 0:
            return []
        characters = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        result = []
        self.solve(digits, characters, result)
        return result

    def solve(self, digits, characters, result, current_string="", current_level=0):
        if current_level == len(digits):
            result.append(current_string)
            return
        for i in characters[int(digits[current_level])]:
            self.solve(digits, characters, result, current_string + i, current_level + 1)


class SolutionV2:
    # Python3 implementation of the approach
    from collections import deque

    # Function to return a list that contains
    # all the generated letter combinations

    def letterCombinationsUtil(self, number, n, table):
        """
        Time Complexity: O(4^n) as we get set of all possible numbers of length n.
                         In worst case, for each number there can be 4 possibilities.
        Auxiliary Space: O(4^n)

        Similar to BFS since queue is used. From GFG's

        :param number:
        :param n:
        :param table:
        :return:
        """

        list = []
        q = deque()
        q.append("")

        while len(q) != 0:
            s = q.pop()

            # If complete word is generated
            # push it in the list
            if len(s) == n:
                list.append(s)
            else:

                # Try all possible letters for current digit
                # in number[]
                for letter in table[number[len(s)]]:
                    print(q)
                    q.append(s + letter)

        # Return the generated list
        return list

    # Function that creates the mapping and
    # calls letterCombinationsUtil
    def letterCombinations(self, number, n):

        # table[i] stores all characters that
        # corresponds to ith digit in phone
        table = ["0", "1", "abc", "def", "ghi", "jkl",
                 "mno", "pqrs", "tuv", "wxyz"]

        return self.letterCombinationsUtil(number, n, table)


if __name__ == "__main__":
    digits = "37"
    print("Letter Combination of {} will be {}".format(
        digits, Solution().letterCombinations(digits)
    ))

    digits = [3, 7, 8]
    print("Letter Combination of {} will be {}".format(
        digits, SolutionV2().letterCombinations(digits, len(digits))
    ))