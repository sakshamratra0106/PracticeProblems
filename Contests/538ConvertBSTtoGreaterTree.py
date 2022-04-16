"""
Problem Statement

https://leetcode.com/problems/convert-bst-to-greater-tree/submissions/
Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

Solution Explained

https://leetcode.com/problems/convert-bst-to-greater-tree/discuss/1951325/Python3-IN-ORDER-DFS-(-*-.-*-)-Explained
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from Tree.Tree import TreeNode


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root, sm):
            if root is None: return sm
            right = traverse(root.right, sm)
            root.val += right
            left = traverse(root.left, root.val)
            return left
        traverse(root, 0)
        return root