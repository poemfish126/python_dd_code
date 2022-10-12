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
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def level_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if root is None:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            level = []
            current_size = len(queue)
            for i in range(current_size):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                left_node = node.left
                right_node = node.right
                if left_node:
                    queue.append(left_node)
                if right_node:
                    queue.append(right_node)
            result.append(level)
        return result


s = Solution()
# print(s.level_order(TreeNode().deserialize("1,#,2,3,#,#,#")))
print(s.level_order(TreeNode().deserialize("1,2,3,#,#,#,#")))
