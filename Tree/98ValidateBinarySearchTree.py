from typing import Optional
from Tree import TreeNode, BinarySearchTree


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root: Optional[TreeNode], mini: Optional[TreeNode], maxi: Optional[TreeNode]) -> bool:
            """

            :param root:
            :param mini:
            :param maxi:
            :return:

            Time Complexity: O(n)
            Auxiliary Space: O(1) if Function Call Stack size is not considered, otherwise O(n)

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
