from typing import (
    List,
)
import collections
from lintcode.DirectedGraphNode import *



class Solution:
    """
        @param root: a TreeNode
        @return: a list of integer
        """

    def topSort(self, graph):
        if graph is None:
            return
        node_to_indegree = self.get_indegree(graph)
        # bfs
        order = []
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        queue = collections.deque(start_nodes)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order

    def get_indegree(self, graph):
        node_to_degree = {i: 0 for i in graph}
        for node in graph:
            for neighbor in node.neighbors:
                node_to_degree[neighbor] += 1
        return node_to_degree


s = Solution()
node127 = DirectedGraphNode(1).deserialize("0,1,2,3#1,4#2,4,5#3,4,5#4#5")
print(s.topSort(node127))
