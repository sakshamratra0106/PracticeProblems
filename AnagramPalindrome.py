import string


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

    def isPlaindrome(self) -> bool:
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
          .format(s, Solution(s).isPlaindrome()))

    s = "A man, a plan, a canal: Panama"
    print("Given string {} is a palindrome ? {}"
          .format(s, Solution(s).isPlaindrome()))
