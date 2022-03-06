from typing import List


def merge1( nums1: List[int], m: int, nums2: List[int], n: int) -> None:
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
    Self created || O(n) time complexity

    """
    i = 0
    j = 0
    for c in range(0, len(nums1) + len(nums2)):
        # print(0,"--",i, " -- ", j, " -- ", nums1)

        # if j == len(nums2)-1 and i == len(nums1)-1:
        #     print(1,"--",i," -- ",j, " -- ", nums1)
        #     # return nums1

        if i >= len(nums1):
            # print(2, "--", i, " -- ", j, " -- ", nums1)
            nums1.append(nums2[j])
            j += 1
        elif nums1[i] <= nums2[j]:
            # print(3, "--", i, " -- ", j, " -- ", nums1)
            i += 1
        else:
            # print(4, "--", i, " -- ", j, " -- ", nums1)
            nums1.insert(i, nums2[j])
            j += 1
        # print("#############################")
    return nums1


if __name__ == '__main__':
    # Driver Program

    # arr1 = [1, 2, 3, 5]
    # arr1.insert(3, 4)
    # print(arr1)

    nums1 = [1, 2, 3]
    nums2 = [2, 5, 6]
    print(merge1(nums1, 3, nums2, 3))

    nums1 = [1, 2, 3, 89, 9, 78]
    nums2 = [2, 5, 6]
    print(merge1(nums1, 6, nums2, 3))
