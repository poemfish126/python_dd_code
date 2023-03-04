from typing import (
    List,
)
import collections
from lintcode.DirectedGraphNode import *

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

    def hasRoute(self, grahp, s, t) -> bool:
        queue = collections.deque([s])
        visited = set([s])

        while queue:
            node = queue.popleft()
            if node == t:
                return True
            for neighber in node.neighbors:
                if neighber in visited:
                    continue
                queue.append(neighber)
                visited.add(neighber)
        return False


s = Solution()
node176 = DirectedGraphNode(1).deserialize("1,2,4#2,3,4#4,5 #3#5")
list_178 = [i for i in node176]
print("a")
# print(s.cloneGraph(UndirectedGraphNode(1).deserialize("1,2,4#2,1,4#3,5#4,1,2#5,3")))
t = s.hasRoute(list_178, list_178[1], list_178[2])
print(t)
