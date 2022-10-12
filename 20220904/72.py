from lintcode.TreeNode import *
from typing import List

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """

    def build_tree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None  # inorder is empty
        root = TreeNode(postorder[-1])
        rootPos = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[: rootPos], postorder[: rootPos])
        root.right = self.buildTree(inorder[rootPos + 1:], postorder[rootPos: -1])
        return root


inorder_traversal = [1, 2, 3]
postorder_traversal = [1, 3, 2]
s = Solution()
print(s.build_tree(inorder_traversal, postorder_traversal))
