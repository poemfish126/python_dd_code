from typing import (
    List,
)


class Solution:

    def max_profit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                profit += prices[i] - prices[i - 1]
        return profit


s = Solution()
print(s.max_profit([2, 1, 2, 0, 1]))
