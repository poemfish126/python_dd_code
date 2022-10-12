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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """

    def zigzag_level_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        order = -1
        while queue:
            level = []
            order *= -1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                left_node = node.left
                right_node = node.right
                if left_node:
                    queue.append(left_node)
                if right_node:
                    queue.append(right_node)

            result.append(level[::order])
        return result


s = Solution()
# print(s.level_order(TreeNode().deserialize("1,#,2,3,#,#,#")))
print(s.zigzag_level_order(TreeNode().deserialize("3,9,20,#,#,15,7,#,#,#,#")))
