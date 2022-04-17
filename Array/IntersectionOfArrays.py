"""Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


Follow up:

1. What if the given array is already sorted? How would you optimize your algorithm?
2. What if nums1's size is small compared to nums2's size?
3. Which algorithm is better? What if elements of nums2 are stored on disk, and the memory is
limited such that you cannot load all elements into the memory at once? """

from typing import List


def intersectOfArray(nums1: List[int], nums2: List[int]) -> List[int]:

    """
    :param nums1: List[int]
    :param nums2: List[int]
    :return: List[int]

    Calculates the Intersection of two array in O(N) time complexity and O(N) Space complexity
    """

    unique_elements_of_nums1 = {}
    common_elements = []
    for element in nums1:
        if element in unique_elements_of_nums1:
            unique_elements_of_nums1[element] += 1
        else:
            unique_elements_of_nums1[element] = 1

    for element in nums2:
        if element in unique_elements_of_nums1 and unique_elements_of_nums1[element] > 0:
            common_elements.append(element)
            unique_elements_of_nums1[element] -= 1

    return common_elements


def intersectOfArray1(nums1: List[int], nums2: List[int]) -> List[int]:

    """
    :param nums1: List[int]
    :param nums2: List[int]
    :return: List[int]

    1. What if the given array is already sorted? How would you optimize your algorithm?
    TC : O(N)
    SC : O(1)
    """

    length1 = len(nums1)
    length2 = len(nums2)

    if length1 == 0 or length2 == 0:
        return []

    i = 0
    j = 0
    common_elements = []
    while i < length1 and j < length2:
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] == nums2[j]:
            common_elements.append(nums1[i])
            i += 1
            j += 1


    return common_elements


if __name__ == '__main__':
    # DriverCode
    nums1 = [1,  3, 4, 5, 2]
    nums2 = [2, 5, 6]
    print("Intersection of the two arrays nums1 : {} and nums2 : {} is : {}"
          .format(nums1, nums2, intersectOfArray(nums1, nums2)))

    nums1 = [1, 2, 3, 4, 5]
    nums2 = [2, 5, 6]
    print("Intersection of the two arrays nums1 : {} and nums2 : {} is : {}"
          .format(nums1, nums2, intersectOfArray1(nums1, nums2)))