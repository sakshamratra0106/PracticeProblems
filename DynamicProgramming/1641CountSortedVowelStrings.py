# https://leetcode.com/problems/count-sorted-vowel-strings/
# https://www.geeksforgeeks.org/count-n-length-strings-consisting-only-of-vowels-sorted-lexicographically/

# Naive Approach: The simplest approach is to generate all possible strings of length N such that
# each string is sorted in lexicographical order. Print the count obtained after completing the steps.
# https://www.geeksforgeeks.org/print-all-combinations-of-given-length/


class Solution:

    # Python3 program to illustrate Count of N-length strings
    # consisting only of vowels sorted lexicographically

    # to keep the string in lexicographically sorted order use
    # start index
    # to add the vowels starting the from that index
    def countstrings(self, n, start):
        """

        Recursive Approach: Keep track of the vowel added to the string so that
        the next vowel added to the string is always Lexicographically greater.

        Time Complexity: O(N!)
        Auxiliary Space: O(1)
        :param n:
        :param start:
        :return:
        """

        # base case: if string length is 0 add to the count
        if n == 0:
            return 1
        cnt = 0

        # if last character in string is 'e'
        # add vowels starting from  'e'
        # i.e    'e','i','o','u'
        for i in range(start, 5):

            # decrease the length of string
            cnt += self.countstrings(n - 1, i)
        return cnt

    def countVowelStrings(self, n):

        #  char arr[5]={'a','e','i','o','u'};
        # starting from index 0 add the vowels to strings
        return self.countstrings(n, 0)

    # Python3 program for the
    # above approach

    # Function to count N-length
    # strings consisting of vowels
    # only sorted lexicographically
    def findNumberOfStrings(n):
        """
        Time Complexity: O(N*5)
        Auxiliary Space: O(N*5)

        :return:
        """

        # Stores count of strings
        # consisting of vowels
        # sorted lexicographically
        # of all possible lengths
        DP = [[0 for i in range(6)]
              for i in range(n + 1)]

        # Initialize DP[1][1]
        DP[1][1] = 1

        # Traverse the matrix row-wise
        for i in range(1, n + 1):
            for j in range(1, 6):

                # Base Case
                if (i == 1):
                    DP[i][j] = DP[i][j - 1] + 1
                else:
                    DP[i][j] = DP[i][j - 1] + DP[i - 1][j]

        # Return the result
        return DP[n][5]

    # Python3 program for the above approach

    # Function to count N-length strings
    # consisting of vowels only sorted
    # lexicographically
    def findNumberOfStringsV1(N):
        """
        Time Complexity: O(5*N)
        Space Complexity: O(1)

        :return:
        """
        # Initializing vector to store count of strings.
        counts = []
        for i in range(5):
            counts.append(1)

        for i in range(2, N + 1):
            for j in range(3, -1, -1):
                counts[j] += counts[j + 1]

        ans = 0

        # Summing up the total number of combinations.
        for c in counts:
            ans += c

        # Return the result
        return ans

    # Python3 program for the
    # above approach

    # Function to count N-length
    # strings consisting of vowels
    # only sorted lexicographically
    def findNumberOfStringsV2(n):
        """
        Time Complexity: O(1)
        Auxiliary Space: O(1)

        :return:
        """
        return int((n + 1) * (n + 2) * (n + 3) * (n + 4) // 24)
