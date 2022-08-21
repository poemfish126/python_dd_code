from typing import (
    List,
)

class Solution:
    """
    @param l: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def wood_cut(self, l: List[int], k: int) -> int:
        # write your code here
        if not l:
            return 0

        start, end = 1, max(l)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_pieces(l, mid) >= k:
                start = mid
            else:
                end = mid

        if self.get_pieces(l, end) >= k:
            return end
        if self.get_pieces(l, start) >= k:
            return start

        return 0

    def get_pieces(self, L, length):
        pieces = 0
        for l in L:
            pieces += l // length
        return pieces


L = [232, 124, 456]
k = 7
s = Solution()
print(s.wood_cut(L, k))
