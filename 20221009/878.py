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
        @param root: a TreeNode
        @return: a list of integer
        """

    def boundary_of_binary_tree(self, root: TreeNode) -> List[int]:
        # write your code here
        if root is None:
            return []
        all_line = []
        queue = collections.deque([(root, 0)])
        while queue:
            size = len(queue)
            line = []
            for i in range(size):
                node, x = queue.popleft()
                if node:
                    line.append((node.val, x))
                if node.left:
                    queue.append((node.left, -1))
                if node.right:
                    queue.append((node.right, 1))
            all_line.append(line)
        result = []
        # put in the first line
        top = all_line[0][0]
        result.append(top[0])
        left = [line[0][0] for line in all_line[1:-1] if line[0][1] < 0]
        if left:
            result.extend(left)
        result.extend([line[0] for line in all_line[-1]])
        right = [line[-1][0] for line in all_line[1:-1] if line[-1][1] > 0 or len(line) > 1]
        if right:
            right.reverse()
            result.extend(right)
        return result

s = Solution()
# print(s.boundary_of_binary_tree(TreeNode().deserialize("1,2,3,4,5,6,#,#,#,7,8,9,10,#,#,#,#,#,#,#,#")))
print(s.boundary_of_binary_tree(TreeNode().deserialize("1,#,2,3,4,#,#,#,#")))
