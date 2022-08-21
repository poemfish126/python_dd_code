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
    @param root: The root of binary tree.
    @return: An integer
    """

    def max_depth(self, root: TreeNode) -> int:
        # write your code here
        if root is None:
            return 0

        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)
        return max(left_depth, right_depth) + 1


s = Solution()
print(s.max_depth(node1023))
print(s.max_depth(node123))
