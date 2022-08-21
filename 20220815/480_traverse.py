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
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
             we will sort your return value in output
    """

    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        # write your code here
        if root is None:
            return []

        self.result = []
        self.traverse(root, '')

        return self.result

    def traverse(self, root: TreeNode, path: str):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.result.append(path + str(root.val))
            return
        new_path = path + str(root.val) + "->"
        if root.left is not None:
            self.traverse(root.left, new_path)
        if root.right is not None:
            self.traverse(root.right, new_path)


s = Solution()
print(s.binary_tree_paths(node1023))
print(s.binary_tree_paths(node1235))
print(s.binary_tree_paths(node12345))
