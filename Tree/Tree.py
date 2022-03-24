from typing import Optional


class TreeNode:
    def __init__(self, val: int):
        self.left = None
        self.val = val
        self.right = None


# Implementing Binary Search Tree
class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    # Insert the value to the Tree
    def insert(self, value: int):

        # Create treenode using the inserted value
        n = TreeNode(value)

        y = None
        temp = self.root

        # finding the parent node
        # where new can become a child node
        while temp is not None:
            y = temp
            if n.val < temp.val:
                temp = temp.left
            else:
                temp = temp.right

        # Incase implementation has parent pointer as well
        # n.parent = y

        # Assign the new child node to the new paren node
        # Or to root itself if the tree was empty before
        if y is None:  # newly added node is root
            self.root = n
        elif n.val < y.val:
            y.left = n
        else:
            y.right = n

    # Inorder traversal of the tree left, root, right
    def inOrderTraversal(self, node: Optional[TreeNode]):
        resultedTree = []
        if node:
            resultedTree = self.inOrderTraversal(node.left)
            resultedTree.append(node.val)
            resultedTree = resultedTree + self.inOrderTraversal(node.right)

        return resultedTree

    # PreOrder traversal of the tree root, left, right
    def preOrderTraversal(self, node: Optional[TreeNode]):
        resultedTree = []
        if node:
            resultedTree.append(node.val)
            resultedTree = resultedTree + self.preOrderTraversal(node.left)
            resultedTree = resultedTree + self.preOrderTraversal(node.right)

        return resultedTree


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

    print("Binary Search Tree Inorder Traversal after inserting is {}".format(
        btree.inOrderTraversal(btree.root)
    ))

    print("Binary Search Tree Pre-Order Traversal after inserting is {}".format(
        btree.preOrderTraversal(btree.root)
    ))
