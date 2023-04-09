from typing import (
    List,
)


class Solution:

    def count_bits(self, num: int) -> List[int]:
        dp_f = [0 for i in range(num + 1)]

        for i in range(1, num + 1):
            dp_f[i] = (i & 1) + dp_f[i >> 1]

        return dp_f


s = Solution()
print(s.count_bits(170))
