from typing import (
    List,
)
import heapq

class Solution:

    def kth_smallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0:
            return None
        minheap = [(matrix[0][0], 0, 0)]
        visited = set([0])
        num = None
        for _ in range(k):
            num, x, y = heapq.heappop(minheap)
            if x + 1 < m and (x + 1) * m + y not in visited:
                visited.add((x + 1) * m + y)
                heapq.heappush(minheap, (matrix[x + 1][y], x + 1, y))
            if y + 1 < n and x * m + y + 1 not in visited:
                visited.add(x * m + y + 1)
                heapq.heappush(minheap, (matrix[x][y + 1], x, y + 1))

        return num


m = [
    [1, 5, 7],
    [3, 7, 8],
    [4, 8, 9],
]
s = Solution()
print(s.kth_smallest(m, 7))
