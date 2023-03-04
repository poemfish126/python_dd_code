from typing import (
    List,
)


class Solution:

    def merge_sorted_array(self, a: List[int], b: List[int]) -> List[int]:
        C = []
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                C.append(a[i])
                i += 1
            else:
                C.append(b[j])
                j += 1
        if i < len(a):
            for n in range(len(a) - i):
                C.append(a[n + i])
        if j < len(b):
            for n in range(len(b) - j):
                C.append(b[n + j])
        return C


A = [1, 2, 3, 4]
B = [2, 4, 5, 6]
s = Solution()
print(s.merge_sorted_array(A, B))
