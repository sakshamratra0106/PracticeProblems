# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None:
            return False
        res_list = list()

        def in_order_traversal(root):
            if root is None:
                return
            in_order_traversal(root.left)
            res_list.append(root.val)
            in_order_traversal(root.right)

        in_order_traversal(root)
        res_list_len = len(res_list)
        left, right = 0, res_list_len - 1
        while left < right:
            if res_list[left] + res_list[right] == k:
                return True
            elif res_list[left] + res_list[right] < k:
                left += 1
            elif res_list[left] + res_list[right] > k:
                right -= 1
        return False

    # Iterative way to complete it
    def findTarget1(self, root: Optional[TreeNode], k: int) -> bool:

        if root == None and k != 0:
            return False

        q1 = deque([root])
        s = set()
        while q1:
            node = q1.popleft()
            if k - node.val in s:
                return True
            s.add(node.val)
            if node.left:
                q1.append(node.left)
            if node.right:
                q1.append(node.right)
        return False
