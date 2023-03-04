from typing import (
    List,
)
import heapq


class Solution:

    def kth_in_arrays(self, arrays: List[List[int]], k: int) -> int:
        m = len(arrays)
        if m == 0:
            return -1
        n = len(arrays[0])
        if n == 0:
            return -1
        # sort all lines
        sorted_a = []
        for arr in arrays:
            if not arr:
                continue
            sorted_a.append(sorted(arr, reverse=True))
        max_heap = [
            (-arr[0], index, 0)
            for index, arr in enumerate(sorted_a)
        ]
        heapq.heapify(max_heap)
        num = None
        for _ in range(k):
            num, x, y = heapq.heappop(max_heap)
            num = -num
            if y + 1 < len(sorted_a[x]):

                heapq.heappush(max_heap, (-sorted_a[x][y + 1], x, y + 1))

        return num


k, a = 2, [[9, 3, 2, 4, 8], [1, 2, 3, 4, 2]]
s = Solution()
print(s.kth_in_arrays(a, k))
