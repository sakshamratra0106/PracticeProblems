from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.val = val
        self.right = None
        self.parent = None


# Implementing Binary Search Tree
class BinarySearchTree:
    def __init__(self, head=None):
        self.head = head

    # Inserting values to the binary search tree
    def insert(self, value: int):
        """

        :param value:
        :return:

        TC : O(N) [If binary tree is skewed]
        TC : O(LogN)
        SC : O(1)

        """
        # Create treenode using the inserted value
        n = TreeNode(value)

        y = None
        temp = self.head

        # finding the parent node
        # where new can become a child node
        while temp:
            y = temp
            if n.val < temp.val:
                temp = temp.left
            else:
                temp = temp.right

        # Incase implementation has parent pointer as well
        # n.parent = y

        # Assign the new child node to the new paren node
        # Or to head itself if the tree was empty before
        if y is None:  # newly added node is head
            self.head = n
        elif n.val < y.val:
            y.left = n
        else:
            y.right = n

    def inOrderTraversal(self, node: Optional[TreeNode]):

        if node:
            self.inOrderTraversal(node.left)
            print(node.val, end=",")
            self.inOrderTraversal(node.right)

    def preOrderTraversal(self, node: Optional[TreeNode]):

        if node:
            print(node.val, end=",")
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)

    def postOrderTraversal(self, node: Optional[TreeNode]):

        if node:
            self.postOrderTraversal(node.left)
            self.postOrderTraversal(node.right)
            print(node.val, end=",")


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

    print("\n Binary Search Tree Inorder Traversal after inserting is {}".format(
        btree.inOrderTraversal(btree.head)
    ))

    print("\n Binary Search Tree Inorder Traversal after inserting is {}".format(
        btree.preOrderTraversal(btree.head)
    ))

    print("\n Binary Search Tree Inorder Traversal after inserting is {}".format(
        btree.postOrderTraversal(btree.head)
    ))
