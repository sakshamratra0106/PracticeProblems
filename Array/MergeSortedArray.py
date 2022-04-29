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

    Lot of slicing happening hence extra time is consumed
    """
    i = 0
    j = 0

    nums1[:] = nums1[:m]

    if m <= 0 or n <= 0:
        nums1[:] = nums1[:] + nums2[:]
        # print("having a corner case where  m <= 0 or n <= 0")
        return

    while i + j < m + n - 1:
        # print(nums1, "--", i, "--", j, "--", nums1[i] > nums2[j], nums1[i], "--", nums2[j])
        if nums1[i] > nums2[j]:
            nums1.insert(i, nums2[j])
            j += 1
        elif i >= m - 1:
            nums1.append(nums2[j])
            j += 1
        else:
            i += 1
        # print("END", nums1)


def mergeArrays(arr1, arr2, n1, n2):
    """

    :param arr1:
    :param arr2:
    :param n1:
    :param n2:
    :return:

    TC O(N+M)
    SC O(N+M)

    """
    arr3 = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0

    # Traverse both array
    while i < n1 and j < n2:

        # Check if current element
        # of first array is smaller
        # than current element of
        # second array. If yes,
        # store first array element
        # and increment first array
        # index. Otherwise do same
        # with second array
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1

    # Store remaining elements
    # of first array
    while i < n1:
        arr3[k] = arr1[i];
        k = k + 1
        i = i + 1

    # Store remaining elements
    # of second array
    while j < n2:
        arr3[k] = arr2[j];
        k = k + 1
        j = j + 1
    print("Array after merging")
    for i in range(n1 + n2):
        print(str(arr3[i]), end=" ")


def mergeOptimized(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    This fills the first array nums1 from backwards.
    No Slicing : No Auxiliary Space Used

    # Time: O(n + m) -> Total length of num1 list
    # Space: O(1)


    """
    length = m + n - 1      #Total length of num1 list
    m = m - 1
    n = n - 1
    for i in range(length, -1, -1):
        if n < 0:                                #Edge case when list2 is null or n -= 1 goes to -1
            break
        if nums1[m] > nums2[n] and m >= 0:       #Edge case when m -= 1 goes to -1
            nums1[i] = nums1[m]
            m -= 1
        else:
            nums1[i] = nums2[n]
            n -= 1


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
