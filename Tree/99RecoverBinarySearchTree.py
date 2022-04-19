# https://leetcode.com/problems/recover-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import islice
from typing import Optional, Iterable

from Tree.Tree import TreeNode


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        max_node = None
        min_node = None
        node_pairs = zip(in_order(root), islice(in_order(root), 1, None))
        for left_node, right_node in node_pairs:
            if left_node.val > right_node.val:
                min_node = right_node
                if max_node is None:
                    max_node = left_node

        if max_node is not None and min_node is not None:
            swap(max_node, min_node)


def swap(node1: TreeNode, node2: TreeNode):
    node1_val = node1.val
    node1.val = node2.val
    node2.val = node1_val


def in_order(root: Optional[TreeNode]) -> Iterable[TreeNode]:
    if root is None:
        return

    for node in in_order(root.left):
        yield node

    yield root

    for node in in_order(root.right):
        yield node