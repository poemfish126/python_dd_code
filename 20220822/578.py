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
    @param: root: The root of the binary tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        a, b, lca = self.helper(root, A, B)
        if a and b:
            return lca
        else:
            return None

    # 每次返回
    # 是否在左子树中找到了节点A，是否在右子树中找到了节点B，以及是否已经找到了LCA，
    # 这三个结果。然后分类讨论。如果已经在子树中找到了LCA, 就直接return。否则，如果当前节点是
    # A且在子树中找到了B，或者当前节点是B且已经在子树中找到了A，就说明当前节点是LCA。
    def helper(self, root, A, B):
        if root is None:
            return False, False, None

        left_a, left_b, left_node = self.helper(root.left, A, B)
        right_a, right_b, right_node = self.helper(root.right, A, B)

        a = left_a or right_a or root == A
        b = left_b or right_b or root == B

        if root == A or root == B:
            return a, b, root

        if left_node is not None and right_node is not None:
            return a, b, root
        if left_node is not None:
            return a, b, left_node
        if right_node is not None:
            return a, b, right_node

        return a, b, None

s = Solution()
print(s.lowestCommonAncestor3(node88, leaf3, leaf5).val)

