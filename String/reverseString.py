from typing import List


class Solution:

    def __init__(self, string):
        self.string = string

    def reverseString(self) -> str:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(self.string) - 1

        while i < j:
            temp = self.string[i]
            self.string[i] = self.string[j]
            self.string[j] = temp
            i += 1
            j -= 1

        return self.string

    def reverseInteger(self) -> int:
        int_to_list = [i for i in self.string]

        # To include the cases when digit is negative
        # This still can not handle when where
        # If reversing x causes the value to go outside the signed 32-bit integer range
        # [-2 power 31, 2 power 31 - 1], then return 0.
        if int_to_list[0] == "-":
            self.string = int_to_list[1:]
            return -int("".join(self.reverseString()))
        else:
            self.string = int_to_list
            return int("".join(self.reverseString()))


if __name__ == "__main__":
    # Run Reverse String using two pointers
    s = ["h", "e", "l", "l", "o"]

    print("Reverse of string : {} will be {}"
          .format(s, Solution(s).reverseString()))

    s1 = ["a", "b", "c", "d"]
    print("Reverse of string : {} will be {}"
          .format(s1, Solution(s1).reverseString()))

    s2 = ["H", "a", "n", "n", "a", "h"]
    print("Reverse of string : {} will be {}"
          .format(s2, Solution(s2).reverseString()))

    # Run Reverse integer using two pointers
    s = 1234
    print("Reverse of string : {} will be {}"
          .format(s, Solution(str(s)).reverseInteger()))

    # Run Reverse integer using two pointers
    s = -1234
    print("Reverse of string : {} will be {}"
          .format(s, Solution(str(s)).reverseInteger()))

    #
