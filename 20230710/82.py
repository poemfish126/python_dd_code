from typing import (
    List,
)


class Solution:

    def single_number(self, a: List[int]) -> int:
        ans = 0
        for x in a:
            ans = ans ^ x
        return ans


A = [1, 1, 2, 2, 3, 4, 4]
s = Solution()
print(s.single_number(A))
