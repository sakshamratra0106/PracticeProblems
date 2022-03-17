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