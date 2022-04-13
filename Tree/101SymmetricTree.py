from collections import deque
from typing import Optional
from Tree import TreeNode, BinarySearchTree


class Solution:

    # Recursive
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """

        :param root:
        :return:

        Time Complexity: O(N) where n is number of nodes in the BST
        Auxiliary Space: O(h) where h is the maximum height of the tree

        """

        return self.isMirror(root.left, root.right)

    def isMirror(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        if root1 is None and root2 is None:
            return True

        if root1 is not None and root2 is not None:

            if root1.val == root2.val:
                return (
                        self.isMirror(root1.left, root2.right) and
                        self.isMirror(root1.right, root2.left)
                )

    # Iterative
    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 1
        q = deque()
        q.append((root.left, root.right))
        while len(q):
            left, right = q.popleft()
            if left is None and right is None:
                continue
            elif left is None or right is None or left.val != right.val:
                return 0
            q.append((left.right, right.left))
            q.append((left.left, right.right))
        return 1


if __name__ == "__main__":
    # Driver Code
    # Let's construct the tree show in the above figure
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print("Symmetric" if Solution().isSymmetric(root) == True else "Not symmetric")
    print("Symmetric" if Solution().isSymmetric1(root) == True else "Not symmetric")
    # This code is contributed by Nikhil Kumar Singh(nickzuck_007)
