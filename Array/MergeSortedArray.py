from typing import List


def merge1(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    Time Complexity is NA
    """
    merged = nums1[:m] + nums2[:n]
    merged.sort()
    nums1[:] = merged
    return nums1


def merge(nums1: List[int], nums2: List[int], m: int = 0, n: int = 0) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    can be better solved using DS as Linked List
    Self created || O(n + m) time complexity
    """
    i = 0
    j = 0

    nums1[:] = nums1[:m]

    if m <= 0 or n <= 0:
        nums1[:] = nums1[:] + nums2[:]
        print("having a corner case where  m <= 0 or n <= 0")
        return

    while i + j < m + n - 1:
        print(nums1, "--", i, "--", j, "--", nums1[i] > nums2[j], nums1[i], "--", nums2[j])
        if nums1[i] > nums2[j]:
            nums1.insert(i, nums2[j])
            j += 1
        elif i >= m - 1:
            nums1.append(nums2[j])
            j += 1
        else:
            i += 1
        # print("END", nums1)


if __name__ == '__main__':
    # Driver Program

    # arr1 = [1, 2, 3, 5]
    # arr1.insert(3, 4)
    # print(arr1)

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    merge(nums1, nums2, 3, 3)
    print(nums1)

    nums1 = [1, 2, 3, 9, 78, 89, ]
    nums2 = [2, 5, 6]
    merge(nums1, nums2, 6, 3)
    print(nums1)

    nums1 = [0]
    nums2 = [1]
    merge(nums1, nums2, 0, 1)
    print(nums1)

    nums1 = [0, 0, 0, 0, 0]
    nums2 = [1, 2, 3, 4, 5]
    merge(nums1, nums2, 0, 5)
    print(nums1)

    nums1 = [4, 0, 0, 0, 0]
    nums2 = [1, 2, 3, 5, 6]
    merge(nums1, nums2, 1, 5)
    print(nums1)
