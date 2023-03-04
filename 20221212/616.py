import collections
from typing import (
    List,
)


class Solution:
    def find_order(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = {i: [] for i in range(num_courses)}
        degrees = [0 for i in range(num_courses)]
        result = []
        for i, j in prerequisites:
            degrees[i] += 1
            edges[j].append(i)
        queue = collections.deque()
        for i in range(num_courses):
            if degrees[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            result.append(node)
            child = edges[node]
            for i in child:
                degrees[i] -= 1
                if degrees[i] == 0:
                    queue.append(i)
        if len(result) == num_courses:
            return result
        return None


s = Solution()
# print(s.find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(s.find_order(2, [[1, 0]]))

