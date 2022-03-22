# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        if root is None:
            return output

        return self.traversal(root, output)

    def traversal(self, root: Optional[TreeNode], output: List[int]) -> List[int]:

        if (root):
            self.traversal(root.left, output)
            self.traversal(root.right, output)
            output.append(root.val)

        return output

    # Iterative method
    def postorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = deque()
        if root:
            stack.append(root)
        while len(stack):
            node = stack.pop()
            result.appendleft(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return list(result)
