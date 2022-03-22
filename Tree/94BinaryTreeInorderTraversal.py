# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        if root is None:
            return output

        return self.traversal(root, output)

    def traversal(self, root: Optional[TreeNode], output: List[int]) -> List[int]:

        if (root):
            self.traversal(root.left, output)
            output.append(root.val)
            self.traversal(root.right, output)

        return output

    # Iterative method
    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        stk, res = [], []
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            res.append(root.val)
            root = root.right
        return res
