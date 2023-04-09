import sys


class Solution:

    def sum_squares(self, n: int) -> int:
        if n < 1:
            return 0

        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            max_j = int(i ** 0.5) + 1
            for j in range(1, max_j):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]


s = Solution()
print(s.sum_squares(13))