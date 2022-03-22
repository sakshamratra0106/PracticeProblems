from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root == None:
            return output

        return self.traversal(root, output)

    def traversal(self, root: Optional[TreeNode], output: List[int]) -> List[int]:

        output.append(root.val)

        if root.left is not None:
            self.traversal(root.left, output)
        if root.right is not None:
            self.traversal(root.right, output)

        return output


# TODO
## Impliment the Tree in two classes like TreeNode and BinaryTree
## after that call above function i.e preorderTraversal

# Recursive Traversal

class AlternateSolution1:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        cur = root

        def preorder(root):
            if not root:
                return
            ans.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return ans


# Iterative Traversal

    # cur = root
    # stack = []
    # ans = []
    # while stack or cur:
    #     if cur:
    #         while cur:
    #             stack.append(cur)
    #             ans.append(cur.val)
    #             cur = cur.left
    #     else:
    #         node = stack.pop()
    #         cur = node.right
    # return ans

# Morris Traversal

class AlternateSolution3:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        cur = root
        while cur:
            if not cur.left:
                ans.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if not prev.right:
                    prev.right = cur
                    ans.append(cur.val)
                    cur = cur.left
                else:

                    prev.right = None
                    cur = cur.right
        return ans