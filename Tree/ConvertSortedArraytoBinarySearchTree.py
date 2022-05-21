from typing import Optional, List

from Tree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """

        :param nums:
        :return:

        Time Complexity: O(n)
        """
        if not nums: return

        m = len(nums) // 2  # select root
        root = TreeNode(nums[m])
        root.left = self.sortedArrayToBST(nums[:m])
        root.right = self.sortedArrayToBST(nums[m + 1:])

        return root

    def preOrder(self, node: Optional[TreeNode]):
        if not node:
            return

        print(node.val, end=", ")
        self.preOrder(node.left)
        self.preOrder(node.right)


arr = [1, 2, 3, 4, 5, 6, 7]
root = Solution().sortedArrayToBST(arr)
print("\n PreOrder Traversal of constructed BST ", Solution().preOrder(root))
