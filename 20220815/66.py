from typing import (
    List,
)

from lintcode.TreeNode import *


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    def preorder_traversal(self, root: TreeNode) -> List[int]:
        # write your code here
        self.results = []
        self.traverse(root)
        return self.results

    def traverse(self, root):
        if root is None:
            return
        self.results.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)


s = Solution()
print(s.preorder_traversal(node1023))
print(s.preorder_traversal(node123))
