from typing import (
    List,
)


class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """

    def find_peak(self, a: List[int]) -> int:
        # write your code here
        start, end = 0, len(a) - 1
        asc = a[0] < a[1]
        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_peak(a[mid], a[mid - 1], a[mid + 1]):
                return mid
            elif self.is_same(a[mid], a[mid - 1], a[mid + 1], asc):
                start = mid
            else:
                end = mid
        return start

    def is_peak(self, p: int, p1: int, p2: int) -> bool:
        return p > p1 and p > p2

    def is_same(self, p: int, p1: int, p2: int, asc: bool) -> bool:
        if asc:
            return p1 < p < p2
        else:
            return p1 > p > p2


A = [1, 2, 1, 3, 4, 5, 7, 6]
# A = [1, 2, 3, 4, 1]
s = Solution()
print(s.find_peak(A))
