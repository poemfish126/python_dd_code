from typing import (
    List,
)


class Solution:
    def reverse_integer(self, n: int) -> int:
        if n == 0:
            return 0
        neg = 1
        if n < 0:
            neg, n = -1, -n
        reverse = 0
        while n > 0:
            reverse = int(reverse * 10 + n % 10)
            n = int(n / 10)
        reverse = reverse * neg
        if reverse < -(1 << 31) or reverse > (1 << 31 - 1):
            return 0
        return reverse


s = Solution()
print(s.reserse_integer(-12345))
