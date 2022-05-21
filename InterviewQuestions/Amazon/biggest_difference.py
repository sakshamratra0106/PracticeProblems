# 4.	Largest and Smallest Value (Competency tested: Scripting (any scripting language) )
# Given an array length 1 or more of integers, return the difference between the largest and smallest values in the array.
# Example:
# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
#
# Answer:

def smallest_larget_difference(array) -> int:
    length = len(array)

    if length == 1:
        # Since smallest and largest number will be same
        return 0
    smallest = array[0]
    largest = array[0]
    for index in range(1, length):
        if array[index] < smallest:
            smallest = array[index]
        elif array[index] > largest:
            largest = array[index]

    return largest - smallest



# Its Time Compelxity will be O(N) and Space Complexity will be O(1)
