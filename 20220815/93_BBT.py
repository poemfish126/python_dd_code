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
    @return: True if this Binary tree is Balanced, or false.
    """
    def is_balanced(self, root: TreeNode) -> bool:
        # write your code here
        is_balance, depth = self.helper(root, 0)
        return is_balance

    def helper(self, root: TreeNode, depth: int):
        if not root:
            return True, depth
        left_b, left_d = self.helper(root.left, depth)
        right_b, right_d = self.helper(root.right, depth)
        is_balance = False
        if left_b and right_b and abs(left_d - right_d) < 2:
            is_balance = True
        return is_balance, max(left_d, right_d) + 1


s = Solution()
print(s.is_balanced(node596))
print(s.is_balanced(node5492810))
