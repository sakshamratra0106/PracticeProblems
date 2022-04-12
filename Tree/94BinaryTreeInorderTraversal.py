# Definition for a binary tree node.
from typing import Optional, List
from Tree import TreeNode, BinarySearchTree


class Solution:
    # Recursive method
    def inorderTraversalR1(self, root: Optional[TreeNode]):
        if root:
            self.inorderTraversalR1(root.left)
            print(root.val, end=",")
            self.inorderTraversalR1(root.right)

    def inorderTraversalR2(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        if root is None:
            return result

        return self.recursiveInorder(root, result)

    def recursiveInorder(self, root: Optional[TreeNode], result: List[int]) -> List[int]:

        if root:
            self.recursiveInorder(root.left, result)
            result.append(root.val)
            self.recursiveInorder(root.right, result)

        return result

    # Iterative method
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """

        :param root:
        :return:

        Time Complexity: O(n)
        Space Complexity : O(n)

        """
        stack, result = [], []

        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result


if __name__ == "__main__":
    print("Creating a Binary Search Tree")
    btree = BinarySearchTree()
    btree.insert(50)
    btree.insert(30)
    btree.insert(20)
    btree.insert(40)
    btree.insert(70)
    btree.insert(60)
    btree.insert(80)

    print("\n Binary Search Tree Inorder Traversal Recursive after inserting is {}".format(
        Solution().inorderTraversalR1(btree.root)
    ))

    print("\n Binary Search Tree Inorder Traversal Recursive after inserting is {}".format(
        Solution().inorderTraversalR2(btree.root)
    ))

    print("\n Binary Search Tree Inorder Traversal Iterative after inserting is {}".format(
        Solution().inorderTraversal(btree.root)
    ))
