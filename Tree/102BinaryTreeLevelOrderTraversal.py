# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """

        :param root:
        :return:

        Time Complexity: O(n) where n is the number of nodes in the binary tree
        Auxiliary Space: O(n) where n is the number of nodes in the binary tree

        """
        if not root:
            return root
        res = []
        q = deque([root])

        while q:
            n = len(q)
            tmp = []
            for i in range(n):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(tmp)
        return res


if __name__ == "__main__":
    # Driver Code
    # Let's construct the tree show in the above figure
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print("For a given tree above {}".format(Solution().levelOrder(root)))