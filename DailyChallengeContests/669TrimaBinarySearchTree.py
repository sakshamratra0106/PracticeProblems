# https://leetcode.com/problems/trim-a-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from Tree.Tree import TreeNode


class Solution:

    # Iterative
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        zero = TreeNode(val=-1, right=root)
        st = [(root, zero)]
        while st:
            node, parent = st.pop()
            if not node: continue

            if node.val < low:
                if node.right:  # left subtree goes away
                    if node.right.val > parent.val:
                        parent.right = node.right
                    else:
                        parent.left = node.right

                    st.append((node.right, parent))
                else:
                    if node.val > parent.val:
                        parent.right = None
                    else:
                        parent.left = None

                continue

            if node.val > high:
                if node.left:  # right subtree goes away
                    if node.left.val > parent.val:
                        parent.right = node.left
                    else:
                        parent.left = node.left

                    st.append((node.left, parent))
                else:
                    if node.val > parent.val:
                        parent.right = None
                    else:
                        parent.left = None

                continue

            st.append((node.left, node))
            st.append((node.right, node))

        return zero.right

    # Recursive
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        if low <= root.val <= high:
            return root
        if root.left is not None:
            return root.left
        else:
            return root.right
