from typing import (
    List,
)
import sys


class Solution:

    def max_profit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        dp = [[-float('inf')] * (5 + 1) for _ in range(n + 1)]
        dp[0][1] = 0
        dp[0][2] = dp[0][3] = dp[0][4] = dp[0][5] = -float('inf')
        for i in range(1, n + 1):
            for j in range(1, 6, 2):
                # max(dp[i - 1][j], dp[i - 1][j - 1] + P_i-1 - P_i-2)
                dp[i][j] = dp[i - 1][j]
                if j >= 2 and i >= 2:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + prices[i - 1] - prices[i - 2])
            for j in range(2, 6, 2):
                # max(dp[i - 1][j] + p1- p2, dp[i - 1][j - 1], f[i - 1][j - 2] + p1 - p2)
                dp[i][j] = dp[i - 1][j - 1]
                if i >= 2:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + prices[i - 1] - prices[i - 2])
                if j >= 3:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 2] + prices[i - 1] - prices[i - 2])
        return max(dp[n][1], dp[n][3], dp[n][5])
        # n = len(prices)
        # dp = [[0 for _ in range(6)] for _ in range(n + 1)]
        # for i in range(1, 6):
        #     dp[0][i] = -sys.maxsize
        # dp[0][1] = 0
        # for i in range(1, n + 1):
        #     # no stock
        #     for j in range(1, 6, 2):
        #         dp[i][j] = dp[i - 1][j]
        #         if j > 1 and i > 1 and dp[i - 1][j - 1] > 0:
        #             dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + prices[i - 1] - prices[i - 2])
        #         print(j)
        # for i in range(1, len(prices)):
        #     if prices[i] - prices[i - 1] > 0:
        #         profit += prices[i] - prices[i - 1]
        # return profit


s = Solution()
print(s.max_profit([4, 4, 6, 1, 1, 4, 2, 5]))
