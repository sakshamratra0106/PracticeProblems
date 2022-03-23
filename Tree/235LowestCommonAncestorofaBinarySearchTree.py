# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
            return root
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return self.lowestCommonAncestor(root.left, p, q)

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        D_q = {q: []}

        def dfs(node, path):
            nonlocal p, q
            if not node:
                return

            if p == node:
                D_q[p] = path[::-1]
            if node == q:
                D_q[q] = path[::-1]

            dfs(node.left, path + [node.left])
            dfs(node.right, path + [node.right])

        dfs(root, [root])

        for n in D_q[q]:
            if n in D_q[p]:
                return n