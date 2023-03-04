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

    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        root = node
        if node is None:
            return
        nodes = self.getAllNodes(node)
        



    def getAllNodes(self, node):
        q = collections.deque([node])
        result = set([node])
        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    q.append(neighbor)
        return result


s = Solution()
# print(s.cloneGraph(UndirectedGraphNode(1).deserialize("1,2,4#2,1,4#3,5#4,1,2#5,3")))
for val in node431:
    val.label
    s.clone_graph(val)
