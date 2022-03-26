import string


class Solution:
    def __init__(self, word: str):
        self.string = word

    def isAnagram(self, word: str) -> bool:
        charCount = {}

        for element in self.string:
            if element in charCount:
                charCount[element] += 1
            else:
                charCount[element] = 1

        for element in word:
            if element not in charCount:
                return False
            else:
                charCount[element] -= 1

        for element in charCount:
            if charCount[element] != 0:
                return False

        return True

    def isPalindrome(self) -> bool:
        valid_characters = string.ascii_letters + string.digits
        potentialPalindrome = ("".join(ch for ch in self.string if ch in valid_characters)).lower()

        i = 0
        j = len(potentialPalindrome) - 1

        while i < j:
            if potentialPalindrome[i] == potentialPalindrome[j]:
                i += 1
                j -= 1
            else:
                return False

        return True

    # Can ransomNote: str can be formed out of
    # magazine: str in O(N) time complexity
    # Working code
    # Leetcode 383. Ransom Note
    def canConstruct(self, magazine: str, ransomNote: str) -> bool:
        charCount = {}
        for char in magazine:
            if char in charCount:
                charCount[char] += 1
            else:
                charCount[char] = 1

        for char in ransomNote:
            if char in charCount:
                charCount[char] -= 1
            else:
                return False

        for char in charCount:
            if charCount[char] < 0:
                return False

        return True


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

    s = ""
    t = ""
    print("Given two strings {} and {} is a anagram ? {}"
          .format(s, t, Solution(s).isAnagram(t)))

    # Printing isPalindrome
    # In O(n) time complexity
    s = "amanaplanacanalpanama"
    print("Given string {} is a palindrome ? {}"
          .format(s, Solution(s).isPalindrome()))

    s = "A man, a plan, a canal: Panama"
    print("Given string {} is a palindrome ? {}"
          .format(s, Solution(s).isPalindrome()))
