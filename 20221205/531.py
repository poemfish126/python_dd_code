from typing import (
    List,
)
import collections
from lintcode.UndirectedGraphNode import *

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

    def sixDegrees(self, graph, s, t) -> int:

        queue = collections.deque([s])
        visited = {s: 0}
        while queue:
            node = queue.popleft()
            if node == t:
                return visited[node]
            for neighbor in node.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited[neighbor] = visited[node] + 1
        return -1


s = Solution()
node531 = UndirectedGraphNode(1).deserialize("1,2#2,1,3#3,2,4#4,3,5#5,4,6#6,5,7#7,6,8#8,7,9#9,8,10#10,9,11#11,10,12#12,11,13#13,12")
list_531 = [i for i in node531]
print(s.sixDegrees(list_531, list_531[11], list_531[0]))


