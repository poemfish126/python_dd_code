from typing import (
    List,
)


class Solution:

    def unique_paths_with_obstacles(self, obstacle_grid: List[List[int]]) -> int:
        m = len(obstacle_grid)
        n = len(obstacle_grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            if obstacle_grid[i][0] != 1:
                dp[i][0] = dp[i - 1][0]

        for j in range(1, n):
            if obstacle_grid[0][j] != 1:
                dp[0][j] = dp[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacle_grid[i][j] != 1:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]


obstacleGrid = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
s = Solution()
print(s.unique_paths_with_obstacles(obstacleGrid))
