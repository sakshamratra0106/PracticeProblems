class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Checking if sub is there in the parent string or not
        # Following function takes two string and
        # compute in Time complexity O(N) and space complexity O(1)

        #         Implement strStr().
        #
        # Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
        #
        # Clarification:
        #
        # What should we return when needle is an empty string? This is a great question to ask during an interview.
        #
        # For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's
        # strStr() and Java's indexOf().

        needleLen = len(needle)

        if needleLen == 0:
            return 0

        for index, char in enumerate(haystack):
            if char == needle[0]:
                if haystack[index:index + needleLen] == needle:
                    return index

        return -1


if __name__ == "__main__":

    print("Checking Needle in a Haystack")

    haystack = "hello"
    needle = "ll"
    print("\nFor a given Haystack \"{}\" and Needle \"{}\". Needle is located at Index: {}".format(
        haystack,needle,Solution().strStr(haystack,needle)
    ))

    haystack = "aaaaa"
    needle = "bba"
    print("\nFor a given Haystack \"{}\" and Needle \"{}\". Needle is located at Index: {}".format(
        haystack, needle, Solution().strStr(haystack, needle)
    ))

    haystack = ""
    needle = ""
    print("\nFor a given Haystack \"{}\" and Needle \"{}\". Needle is located at Index: {}".format(
        haystack, needle, Solution().strStr(haystack, needle)
    ))