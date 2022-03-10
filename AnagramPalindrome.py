class Solution:
    def __init__(self, s: str):
        self.string = s

    def isAnagram(self, t: str) -> bool:
        charCount = {}
        for element in self.string:
            if element in charCount:
                charCount[element] += 1
            else:
                charCount[element] = 1

        for element in t:
            if element not in charCount:
                return False
            else:
                charCount[element] -= 1

        for element in charCount:
            if charCount[element] != 0:
                return False

        return True

    def isPlaindrome(self, t: str) -> bool:
        pass

if __name__ == "__main__":
    # Anagram in O(n) time complexity

    s = "anagram"
    t = "nagaram"
    print("Given two strings {} and {} is a anagram ? {}"
          .format(s, t, Solution(s).isAnagram(t)))

    s = "rat"
    t = "car"
    print("Given two strings {} and {} is a anagram ? {}"
          .format(s, t, Solution(s).isAnagram(t)))