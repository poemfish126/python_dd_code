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
    @return: the root of the maximum average of subtree
    """

    def __init__(self):
        self.max_avg = -100000
        self.max_node = None

    def find_subtree2(self, root: TreeNode) -> TreeNode:
        # write your code here
        self.helper(root)
        return self.max_node

    def helper(self, root: TreeNode):
        if not root:
            return 0, 0
        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)
        avg = (root.val + left_sum + right_sum) / (left_size + right_size + 1)
        if avg > self.max_avg:
            self.max_avg = avg
            self.max_node = root
        return (root.val + left_sum + right_sum), left_size + right_size + 1


s = Solution()
print(s.find_subtree2(node596).val)
