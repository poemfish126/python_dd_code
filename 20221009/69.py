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

    @staticmethod
    def level_order(root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = collections.deque([root]);

        while queue:
            size = len(queue)
            line = []
            for i in range(size):
                node = queue.popleft()
                if node:
                    line.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(line)

        return result


# print(s.level_order(TreeNode().deserialize("1,#,2,3,#,#,#")))
print(Solution.level_order(TreeNode().deserialize("1,2,3,#,#,#,#")))
