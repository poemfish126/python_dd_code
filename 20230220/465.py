from typing import (
    List,
)
import heapq


class Solution:

    def kth_smallest_sum(self, a: List[int], b: List[int], k: int) -> int:
        m, n = len(a), len(b)
        if m == 0 or n == 0:
            return None
        minheap = [(a[0] + b[0], 0, 0)]
        visited = set([0])
        num = None
        for _ in range(k):
            num, x, y = heapq.heappop(minheap)
            if x + 1 < m and (x + 1) * n + y not in visited:
                visited.add((x + 1) * n + y)
                heapq.heappush(minheap, (a[x + 1] + b[y], x + 1, y))
            if y + 1 < n and x * n + y + 1 not in visited:
                visited.add(x * n + y + 1)
                heapq.heappush(minheap, (a[x] + b[y + 1], x, y + 1))
        return num


a = [1, 7, 11]
b = [2, 4, 6]
k = 3
s = Solution()
print(s.kth_smallest_sum(a, b, k))
a = [1, 7, 11]
b = [2, 4, 6]
k = 4
print(s.kth_smallest_sum(a, b, k))
