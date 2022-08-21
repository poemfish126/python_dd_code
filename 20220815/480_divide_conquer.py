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
        if root.right is None and root.left is None:
            return [str(root.val)]
        left_list = self.binary_tree_paths(root.left)
        right_list = self.binary_tree_paths(root.right)
        result = []
        for i in left_list:
            result.append(str(root.val) + "->" + i)
        for i in right_list:
            result.append(str(root.val) + "->" + i)
        return result


s = Solution()
print(s.binary_tree_paths(node1023))
print(s.binary_tree_paths(node1235))
print(s.binary_tree_paths(node12345))
