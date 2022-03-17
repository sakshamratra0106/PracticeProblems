# Subarray/Substring
#
# A subarray is a contiguous part of array. An array that is inside another array. For example, consider the array [1, 2, 3, 4], There are 10 non-empty sub-arrays. The subarrays are (1), (2), (3), (4), (1,2), (2,3), (3,4), (1,2,3), (2,3,4) and (1,2,3,4). In general, for an array/string of size n, there are n*(n+1)/2 non-empty subarrays/substrings.
#
# How to generate all subarrays?
# We can run two nested loops, the outer loop picks starting element and inner loop considers all elements on right of the picked elements as ending element of subarray.
#
# Time Complexity: 0(n^3)
#
# Space Complexity: 0(1)

def subArrays(arr):
    n = len(arr)

    for i in range(0, n):
        for j in range(i, n):
            for k in range(i, j + 1):
                print(arr[k], end=" ")
            print("\n", end="")


# Subsequence
# A subsequence is a sequence that can be derived from another sequence by removing zero or more elements, without changing the order of the remaining elements.
# For the same example, there are 15 sub-sequences. They are (1), (2), (3), (4), (1,2), (1,3),(1,4), (2,3), (2,4), (3,4), (1,2,3), (1,2,4), (1,3,4), (2,3,4), (1,2,3,4). More generally, we can say that for a sequence of size n, we can have (2n-1) non-empty sub-sequences in total.
# A string example to differentiate: Consider strings “geeksforgeeks” and “gks”. “gks” is a subsequence of “geeksforgeeks” but not a substring. “geeks” is both a subsequence and subarray. Every subarray is a subsequence. More specifically, Subsequence is a generalization of substring.
#
# A subarray or substring will always be contiguous, but a subsequence need not be contiguous. That is, subsequences are not required to occupy consecutive positions within the original sequences. But we can say that both contiguous subsequence and subarray are the same.
#
# How to generate all Subsequences?
# We can use algorithm to generate power set for generation of all subsequences.

# Python3 code to generate all
# possible subsequences.
# Time Complexity O(n * 2 ^ n)
import math


def printSubsequences(arr, n):
    # Number of subsequences is (2**n -1)
    # Power Set
    opsize = math.pow(2, n)
    # print("opsize ::",opsize)
    # print("Int operation on opsize", int(opsize))
    # Run from counter 000..1 to 111..1
    for counter in range(1, int(opsize)):
        for j in range(0, n):

            # Check if jth bit in the counter
            # is set If set then print jth
            # element from arr[]

            # And operation on ints in Python will result in int of and of respective binary numbers
            # Example : 4 & 4 is 4, 1 & 2 is 0 or 4 & 2 is 0
            # print(counter," | ",j," | ", (1 << j)," | ")
            if counter & (1 << j):
                print(arr[j], end=" ")

        print()
    # This code is contributed by Nikita Tiwari.


##Generating SubArray Using Recursion
# Python3 code to print all possible subarrays
# for given array using recursion

# Recursive function to print all possible subarrays
# for given array
def printSubArrays(arr, start, end):
    # Stop if we have reached the end of the array
    if end == len(arr):
        return

    # Increment the end point and start from 0
    elif start > end:
        return printSubArrays(arr, 0, end + 1)

    # Print the subarray and increment the starting
    # point
    else:
        print(arr[start:end + 1])
        return printSubArrays(arr, start + 1, end)


# MAX sum of a contigous sub array

# Naive Approach: The naive approach is to generate all the possible subarray and print that subarray which has maximum sum.
# Time complexity: O(N2)
# Auxiliary Space: O(1)
#
# Efficient Approach: The idea is to use the Kadane’s Algorithm to find the maximum subarray sum and store the starting and ending index of the subarray having maximum sum and print the subarray from starting index to ending index. Below are the steps:
# O(n)
# Initialize 3 variables endIndex to 0, currMax and globalMax to first value of the input array.
# For each element in the array starting from index(say i) 1, update currMax to max(nums[i], nums[i] + currMax) and globalMax and endIndex to i only if currMax > globalMax.
# To find the start index, iterate from endIndex in the left direction and keep decrementing the value of globalMax until it becomes 0. The point at which it becomes 0 is the start index.
# Now print the subarray between [start, end].

# Python3 program for the above approach

# Function to print the elements
# of Subarray with maximum sum
def SubarrayWithMaxSum(nums):
    curMax = nums[0]
    globalMax = nums[0]
    endIndex = 0

    for i in range(1, len(nums)):

        curMax = max(nums[i], curMax + nums[i])

        if curMax > globalMax:
            globalMax = curMax
            endIndex = i

    startIndex = endIndex

    while (startIndex > 0):
        globalMax -= nums[startIndex]

        if globalMax == 0:
            break

        startIndex -= 1

    return nums[startIndex:endIndex + 1]


# Max SubArray using Divide and conquor :: O(n Log n)
# A Divide and Conquer based program
# for maximum subarray sum problem

# Find the maximum possible sum in
# arr[] auch that arr[m] is part of it


def maxCrossingSum(arr, l, m, h):
    # Include elements on left of mid.
    sm = 0
    left_sum = -10000

    for i in range(m, l - 1, -1):
        sm = sm + arr[i]

        if sm > left_sum:
            left_sum = sm

    # Include elements on right of mid
    sm = 0
    right_sum = -1000
    for i in range(m + 1, h + 1):
        sm = sm + arr[i]

        if (sm > right_sum):
            right_sum = sm

    # Return sum of elements on left and right of mid
    # returning only left_sum + right_sum will fail for [-2, 1]
    return max(left_sum + right_sum, left_sum, right_sum)


# Returns sum of maximum sum subarray in aa[l..h]
def maxSubArraySum(arr, l, h):
    # Base Case: Only one element
    if (l == h):
        return arr[l]

    # Find middle point
    m = (l + h) // 2

    # Return maximum of following three possible cases
    # a) Maximum subarray sum in left half
    # b) Maximum subarray sum in right half
    # c) Maximum subarray sum such that the
    #	 subarray crosses the midpoint
    return max(maxSubArraySum(arr, l, m),
               maxSubArraySum(arr, m + 1, h),
               maxCrossingSum(arr, l, m, h))


if __name__ == '__main__':
    # Driver || Iterative subArray/SubString
    subArrays([1, 2, 3, 4])

    # Driver program || Non-empty Subsequences
    arr = [1, 2, 3, 4]
    n = len(arr)
    print("All Non-empty Subsequences")
    printSubsequences(arr, n)

    ## Driver code ## Recursive SubArray/SubString
    arr = [1, 2, 3, 4]
    printSubArrays(arr, 0, 0)

    ##https://www.geeksforgeeks.org/print-the-maximum-subarray-sum/
    # Driver Code
    # Given array arr[]
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    arr1 = [1]
    arr2 = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

    # Function call
    print("Printing Max Subarray Sum")
    print(SubarrayWithMaxSum(arr), sum(SubarrayWithMaxSum(arr)))
    print(SubarrayWithMaxSum(arr1), sum(SubarrayWithMaxSum(arr1)))
    print(SubarrayWithMaxSum(arr2), sum(SubarrayWithMaxSum(arr2)))

    # Max SubArray using Divide and conquor :: O(n Log n)
    # Driver Code
    arr = [2, 3, 4, 5, 7]
    n = len(arr)
    max_sum = maxSubArraySum(arr, 0, n - 1)
    print("Maximum contiguous sum is ", max_sum)
