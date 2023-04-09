from typing import (
    List,
)


class Solution:
    def house_robber(self, a: List[int]) -> int:
        if not a:
            return 0
        n = len(a)
        if n == 1:
            return a[0]
        if n == 2:
            return max(a[0], a[1])
        f_a = [0 for _ in range(n + 1)]
        old = 0
        new = a[0]
        for i in range(2, n + 1):
            t = max(new, old + a[i - 1])
            old = new
            new = t
        return new


a = [5, 2, 1, 3]
a = [3, 8, 4]
s = Solution()
print(s.house_robber(a))
