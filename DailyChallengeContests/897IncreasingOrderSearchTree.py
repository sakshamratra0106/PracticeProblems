# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Tree.Tree import TreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root: TreeNode, node: TreeNode):
            if root is not None:
                node = inorder(root.left, node)

                node.right = TreeNode(val=root.val)

                node = inorder(root.right, node.right)

            return node

        newRoot = TreeNode()
        inorder(root, newRoot)

        return newRoot.right

