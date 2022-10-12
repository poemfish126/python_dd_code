import collections
from typing import (
    List,
)
from lintcode.UndirectedGraphNode import *


class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """

    def connectedSet(self, nodes: List[UndirectedGraphNode]) -> List[List[int]]:
        # write your code here
        result = []
        visited = set()

        for node in nodes:
            if node not in visited:
                subgraph = []
                self.bfs(node, visited, subgraph)
                result.append(sorted(subgraph))
        return result

    def bfs(self, node, visited, subgraph):
        queue = collections.deque()
        queue.append(node)
        visited.add(node)

        while queue:
            node = queue.popleft()
            subgraph.append(node.label)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


s = Solution()
print(s.connectedSet(node431))
