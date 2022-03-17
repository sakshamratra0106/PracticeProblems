class Solution:

    def __init__(self, integer: int):
        self.integer = integer

    def reverse(self) -> int:
        reverseInt = 0
        pop = 0
        tmp = abs(self.integer)

        # when input number is zero
        if self.integer == 0:
            return 0

        while tmp > 0:
            pop = tmp % 10
            tmp = int(tmp / 10)
            reverseInt = reverseInt * 10 + pop
            if reverseInt < - 2 ** 31 or reverseInt > 2 ** 31 - 1:
                return 0
            # print(pop, "--", tmp, "--", reverseInt)

        return int(reverseInt * self.integer / abs(self.integer))


if __name__ == "__main__":
    # Reverse integer
    #     Given a signed 32-bit integer x, return x with its digits reversed.
    #     If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
    #     then return 0.
    #
    # Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

    # Positive Number
    integer1 = 123456
    print("Reverse Integer of given integer : {} is {}"
          .format(integer1, Solution(integer1).reverse()))

    # Negative Number
    integer1 = -123456
    print("Reverse Integer of given integer : {} is {}"
          .format(integer1, Solution(integer1).reverse()))

    # Number greater than 2 ** 31 -1
    integer1 = -1294967296
    print("Reverse Integer of given integer : {} is {}"
          .format(integer1, Solution(integer1).reverse()))

    # Number is Zero
    integer1 = -0
    print("Reverse Integer of given integer : {} is {}"
          .format(integer1, Solution(integer1).reverse()))