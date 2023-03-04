from typing import (
    List,
)
import collections
from lintcode.DirectedGraphNode import *


class Solution:

    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        edges = {i: [] for i in range(num_courses)}
        degrees = [0 for i in range(num_courses)]
        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1
        queue, count = collections.deque([]), 0
        for i in range(num_courses):
            if degrees[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            count += 1
            for x in edges[node]:
                degrees[x] -= 1
                if degrees[x] == 0:
                    queue.append(x)

        return count == num_courses


s = Solution()
print(s.can_finish(2, [[1, 0]]))
