from typing import (
    List,
)
from lintcode.TreeNode import *


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        # write your code here
        self.result = []
        self.traverse(root)
        return self.result

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        self.result.append(root.val)
        self.traverse(root.right)


s = Solution()
print(s.inorder_traversal(node1023))
print(s.inorder_traversal(node123))


