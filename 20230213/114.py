class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]
        for j in range(n):
            dp[0][j] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]


s = Solution()
print(s.unique_paths(401, 30))
