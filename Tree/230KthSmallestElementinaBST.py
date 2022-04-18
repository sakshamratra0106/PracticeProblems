from typing import Optional
from Tree.Tree import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pos = 0
        ans = 0

        current = root

        while current and pos < k:

            if not current.left:
                pos += 1
                ans = current.val
                current = current.right

            else:
                pre = current.left
                while pre.right:
                    pre = pre.right

                pre.right = current
                left = current.left
                current.left = None
                current = left

        return ans