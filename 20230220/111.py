class Solution:

    def climb_stairs(self, n: int) -> int:
        n += 1
        if n == 0 or n == 1:
            return 1
        #  state: distinct ways for i step
        dp = [0 for i in range(n)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]

s = Solution()
print(s.climb_stairs(2))