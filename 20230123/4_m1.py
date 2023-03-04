import sys
from typing import (
List,
)

class Solution:

    def nth_ugly_number(self, n: int) -> int:
        count = 0
        for i in range(sys.maxsize):
            if self.is_ugly(i):
                count += 1
            if count == n:
                return i
        return count

    def is_ugly(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        while num >= 2 and num % 2 == 0:
            num /= 2
        while num >= 3 and num % 3 == 0:
            num /= 3
        while num >= 5 and num % 5 == 0:
            num /= 5
        return num == 1

s = Solution()
print(s.nth_ugly_number(599))
