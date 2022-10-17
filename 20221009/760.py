from typing import (
    List,
)
import collections
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
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """

    def right_side_view(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        queue = collections.deque([root])
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

        return [line[-1] for line in result]


s = Solution()
print(s.right_side_view(TreeNode().deserialize("1,#,2,3,#,#,#")))
