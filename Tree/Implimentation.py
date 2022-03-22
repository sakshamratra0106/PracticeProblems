# Two kind of implementation using One class (TreeNode and BinaryTree) or (BinaryTree)
# Explanation for the above is mentioned in below link
# https://stackoverflow.com/questions/65743957/is-it-a-mandatory-to-have-two-classesnode-tree-while-implementing-a-binary-tre


# Second kind of implementation

class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent BinaryTree
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

            # Print the tree

    def PrintTree(self):
        # This is more of an inorder traversal
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    # Inorder traversal
    # Left -> Root -> Right

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    # Preorder traversal
    # Root -> Left ->Right

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    # Postorder traversal
    # Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []

        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res


if __name__ == "__main__":
    # Use the insert method to add nodes
    root = BinaryTree(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.PrintTree()

    # Inorder traversal
    root = BinaryTree(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    print("Creating a tree ")
    root.PrintTree()
    print(root.inorderTraversal(root))

    # Preorder traversal
    print("Creating a pre order traversal ")
    print(root.PreorderTraversal(root))

    # Postorder traversal
    print("Creating a post order traversal ")
    print(root.PostorderTraversal(root))