import math
from typing import Optional
from Tree import TreeNode, BinarySearchTree


class Solution:

    # Approach 1: Recursive Traversal with Valid Range
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root: Optional[TreeNode], mini: Optional[TreeNode], maxi: Optional[TreeNode]) -> bool:
            """

            :param root:
            :param mini:
            :param maxi:
            :return:

            Time complexity : \mathcal{O}(N)O(N) since we visit each node exactly once.
            Space complexity : \mathcal{O}(N)O(N) since we keep up to the entire tree.


            """
            # base case
            if root is None:
                return True
            if mini is not None and root.val <= mini.val:
                return False
            if maxi is not None and root.val >= maxi.val:
                return False
            return isValid(root.left, mini, root) and isValid(root.right, root, maxi)

        return isValid(root, None, None)

    # Approach 2: Iterative Traversal with Valid Range
    def isValidBST1(self, root: TreeNode) -> bool:
        """

        :param root:
        :return:

        Complexity Analysis

        Time complexity : \mathcal{O}(N)O(N) since we visit each node exactly once.
        Space complexity : \mathcal{O}(N)O(N) since we keep up to the entire tree.

        """

        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True

    # Approach 3: Recursive Inorder Traversal
    def isValidBST2(self, root: TreeNode) -> bool:
        """

        :param root:
        :return:


        Complexity Analysis

        Time complexity : \mathcal{O}(N)O(N) in the worst case when the tree is a BST or the "bad" element is a rightmost leaf.

        Space complexity : \mathcal{O}(N)O(N) for the space on the run-time stack.
        """

        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -math.inf
        return inorder(root)

    # Approach 4: Iterative Inorder Traversal
    def isValidBST3(self, root: TreeNode) -> bool:
        """

        :param root:
        :return:

        Complexity Analysis

        Time complexity : \mathcal{O}(N)O(N) in the worst case when the tree is BST or the "bad" element is a rightmost leaf.

        Space complexity : \mathcal{O}(N)O(N) to keep stack.
        """

        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True


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
    btree.insert(91)

    print("\n Binary Search Tree Inorder Traversal after inserting is above".format(
        btree.inOrderTraversal(btree.root)
    ))

    print("\n Binary Search Tree isValidBST i.e is a valid Binary Search Tree : {}".format(
        Solution().isValidBST(btree.root)
    ))

    # Tried creating a  wrong Binary Search Tree
    # But did not work
    ## TODO
    # Implement creating a wrong BST

    # print("Creating a Wrong Binary Search Tree")
    # btree = BinarySearchTree()
    # btree.insertBinarySearchTreeWrongly(50)
    # btree.insertBinarySearchTreeWrongly(30)
    # btree.insertBinarySearchTreeWrongly(20)
    # btree.insertBinarySearchTreeWrongly(40)
    # btree.insertBinarySearchTreeWrongly(70)
    # btree.insertBinarySearchTreeWrongly(60)
    # btree.insertBinarySearchTreeWrongly(80)
    # btree.insertBinarySearchTreeWrongly(91)
    #
    # print("\n Binary Search Tree Inorder Traversal Recursive after inserting is {}".format(
    #     Solution().isValidBST(btree.root)
    # ))
