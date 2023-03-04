from lintcode.TreeNode import *


class Solution:

    def cloneTree(self, root):
        if root is None:
            return None
        node = TreeNode(root.val)
        node.left = self.cloneTree(root.left)
        node.right = self.cloneTree(root.right)
        return node

