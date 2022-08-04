from typing import (
    List,
)


class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copy_books(self, pages: List[int], k: int) -> int:
        # write your code here
        n = len(pages)
        if n == 0:
            return 0
        l = max(pages)
        r = sum(pages)
        while l < r:
            mid = (l + r) // 2
            if self.ok(pages, k, mid):
                r = mid
            else:
                l = mid + 1
        return l

    def ok(self, pages, k, tm):
        num = 1
        pageSum = 0
        for i in pages:
            if pageSum + i <= tm:
                pageSum += i
            else:
                num += 1
                pageSum = i
        return num <= k


pages = [3, 2, 4]
k = 2
s = Solution()
print(s.copy_books(pages, k))
