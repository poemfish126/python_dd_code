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
            return node

        # use bfs algorithm to traverse the graph and get all nodes.
        nodes = self.getNodes(node)

        # copy nodes, store the old->new mapping information in a hash map
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)

        # copy neighbors(edges)
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    def getNodes(self, node):
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
