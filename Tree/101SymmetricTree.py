# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 1
        q=deque()
        q.append((root.left,root.right))
        while len(q):
            left,right=q.popleft()
            if left is None and right is None :
                continue
            if left is None or right is None or left.val!=right.val:
                return 0
            q.append((left.right,right.left))
            q.append((left.left,right.right))
        return 1