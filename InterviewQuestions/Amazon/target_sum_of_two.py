# 5.	Get index (Competency tested: Scripting (any scripting language) )
# Given a list of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# return [0, 1]
# Answer:

def sum_of_two(nums, target) -> list[int]:
    seen = {}
    for index, element in enumerate(nums):
        difference = target - element
        if difference in seen:
            return [seen[difference], index]
        seen[element] = index

    return None


# Its Time Compelxity will be O(N) and Space Complexity will be O(N)
# Incase we want to reduce Space complexity we will an input which is sorted. The we could make TC : O(N) and SC : O(1)



def sum_of_two(nums, target) -> list[int]:
    length = len(nums)

    # IF array is of length less then 2
    if length <= 1:
        return None


    smaller_index = 0
    largest_index = length - 1
    while smaller_index < largest_index:
        if nums[smaller_index] + nums[largest_index] == target:
            return smaller_index, largest_index
        elif nums[smaller_index] + nums[largest_index] > target:
            largest_index -= 1
        elif nums[smaller_index] + nums[largest_index] < target:
            smaller_index += 1

    return None
