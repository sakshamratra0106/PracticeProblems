# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        # post order traversal
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # Swapping left and right child
        root.left, root.right = right, left

        return root
