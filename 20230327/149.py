from typing import (
List,
)
import sys
class Solution:

    def maxProfit(self, prices):
        total = 0
        low, high = sys.maxsize, 0
        for i in prices:
            if i - low > total:
                total = i - low
            if i < low:
                low = i
        return total

prices = [3, 2, 3, 1, 2]
s = Solution()
print(s.maxProfit(prices))
