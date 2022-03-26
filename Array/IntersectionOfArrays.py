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


if __name__ == '__main__':
    # DriverCode
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [2, 5, 6]
    print("Intersection of the two arrays nums1 : {} and nums2 : {} is : {}"
          .format(nums1, nums2, intersectOfArray(nums1, nums2)))
