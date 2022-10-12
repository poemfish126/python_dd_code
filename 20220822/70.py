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
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """

    def level_order_bottom(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if not root:
            return []
        queue = collections.deque([root])
        stack = []
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                left_node = node.left
                right_node = node.right
                if left_node:
                    queue.append(left_node)
                if right_node:
                    queue.append(right_node)
            stack.append(level)
        result = []
        for _ in range(len(stack)):
            result.append(stack.pop())
        return result


s = Solution()
# print(s.level_order(TreeNode().deserialize("1,#,2,3,#,#,#")))
print(s.level_order_bottom(TreeNode().deserialize("3,9,20,#,#,15,7,#,#,#,#")))
