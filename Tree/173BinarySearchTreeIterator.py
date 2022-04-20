## https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        # get the in order tree node values
        def inorder(root):
            if not root:    return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        self.treenodes = inorder(root)

    def next(self):
        # pop out the current smallest int
        return self.treenodes.pop(0)

    def hasNext(self):
        # check if there are remaining int
        return len(self.treenodes) != 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
