import sys

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
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def __init__(self):
        self.min_node = None
        self.min_value = sys.maxsize

    def find_subtree(self, root: TreeNode) -> TreeNode:
        # write your code here
        self.node_sum(root)
        return self.min_node

    def node_sum(self, root: TreeNode) -> int:
        if not root:
            return 0
        sum = root.val + self.node_sum(root.left) + self.node_sum(root.right)
        if sum < self.min_value:
            self.min_value = sum
            self.min_node = root
        return sum


s = Solution()
print(s.find_subtree(node596).val)
