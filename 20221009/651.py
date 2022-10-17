import collections
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
    @param root: the root of tree
    @return: the vertical order traversal
    """

    @staticmethod
    def vertical_order(root: TreeNode) -> List[List[int]]:
        # write your code here
        if root is None:
            return []
        result = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            node, x = queue.popleft()
            if node:
                result[x].append(node.val)
            if node.left:
                queue.append((node.left, x-1))
            if node.right:
                queue.append((node.right, x + 1))

        return [result[i] for i in sorted(result)]


print(Solution.vertical_order(TreeNode().deserialize("3,9,20,#,#,15,7,#,#,#,#")))
