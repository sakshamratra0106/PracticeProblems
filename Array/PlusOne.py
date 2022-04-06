from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """

        :param digits:
        :return:
        TC : O(N)
        SC : O(1)

        """

        length = len(digits)
        for i in range(length - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0

        # Incase digits has been iterated and there is still a carry forward and 0th index is zero
        # carryForward will goto 0 index
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    digits = [4, 3, 2, 1]
    print("1. If digits {} will be added one will become {}".format(
        digits, Solution().plusOne(digits)
    ))

    digits = [9]
    print("2. If digits {} will be added one will become {}".format(
        digits, Solution().plusOne(digits)
    ))

    digits = [8, 9, 9, 9]
    print("3. If digits {} will be added one will become {}".format(
        digits, Solution().plusOne(digits)
    ))

    digits = [8, 9, 8, 9]
    print("3. If digits {} will be added one will become {}".format(
        digits, Solution().plusOne(digits)
    ))