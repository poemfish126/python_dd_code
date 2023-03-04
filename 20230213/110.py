from typing import (
    List,

)


class Solution:

    def min_path_sum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        sum_g = [[0 for j in range(n)] for i in range(m)]
        sum_g[0][0] = grid[0][0]
        for i in range(1, n):
            sum_g[0][i] = sum_g[0][i - 1] + grid[0][i]
        for i in range(1, m):
            sum_g[i][0] = sum_g[i - 1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                sum_g[i][j] = min(sum_g[i][j - 1], sum_g[i - 1][j]) + grid[i][j]
        return sum_g[m - 1][n - 1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
s = Solution()
print(s.min_path_sum(grid))