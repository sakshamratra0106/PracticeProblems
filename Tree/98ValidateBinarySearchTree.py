from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root: Optional[TreeNode], mini: Optional[TreeNode], maxi: Optional[TreeNode]) -> bool:
            # base case
            if root is None:
                return True
            if mini is not None and root.val <= mini.val:
                return False
            if maxi is not None and root.val >= maxi.val:
                return False
            return isValid(root.left, mini, root) and isValid(root.right, root, maxi)

        return isValid(root, None, None)
