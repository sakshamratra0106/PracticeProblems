class Solution:

    def validPalindrome(self, s: str) -> bool:
        """

        :param s:
        :return:

        Checks if the string is a palindrome with at most one deletion of a character .
        Time Complexity : O(N)
        Space Complexity : (1)
        """

        # Function to check if string a palindrome from index i to j
        def check_palindrome(s, i, j) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        # If the string is of zero length return True
        if s is None:
            return True

        # Declare two pointers start and end
        start = 0
        end = len(s) - 1

        # Check for palindrome and skip one character if it isn't
        while start < end:

            # Found a misMatch skip one element from left or right
            if s[start] != s[end]:
                return check_palindrome(s, start + 1, end) or check_palindrome(s, start, end - 1)

            start += 1
            end -= 1

        # Return True if all cases passed
        return True


if __name__ == "__main__":

    givenString = "aba"
    print("1. Given string \"{}\" is a Palindrome with at most one deletion of a character ? {}".format(
        givenString, Solution().validPalindrome(givenString)
    ))

    givenString = "abca"
    print("2. Given string \"{}\" is a Palindrome with at most one deletion of a character ? {}".format(
        givenString, Solution().validPalindrome(givenString)
    ))

    givenString = "abc"
    print("3. Given string \"{}\" is a Palindrome with at most one deletion of a character ? {}".format(
        givenString, Solution().validPalindrome(givenString)
    ))