import collections
from typing import (
    List,
)


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if len(edges) != (n - 1):
            return False
        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        queue = collections.deque()
        visit = {}
        queue.append(0)
        visit[0] = False
        while len(queue) > 0:
            cur = queue.popleft()
            visit[cur] = True
            for node in neighbors[cur]:
                if node not in visit:
                    queue.append(node)
                    visit[node] = True
        return len(visit) == n


n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
edges = [[0, 1], [1, 2], [2, 3], [1, 3]]
s = Solution()
print(s.valid_tree(n, edges))
