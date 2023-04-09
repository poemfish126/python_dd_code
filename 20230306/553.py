from typing import (
    List,
)


class Solution:

    def max_killed_enemies(self, grid: List[List[str]]) -> int:
        i, j, res = 0, 0, 0
        m = len(grid)
        n = len(grid[0])

        dp_up = [[0 for j in range(n)] for i in range(m)]
        dp_left = [[0 for j in range(n)] for i in range(m)]
        dp_down= [[0 for j in range(n)] for i in range(m)]
        dp_right = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W':
                    dp_up[i][j] = 0
                    dp_left[i][j] = 0
                    continue
                if grid[i][j] == 'E':
                    dp_up[i][j] = 1
                    dp_left[i][j] = 1
                if i > 0:
                    dp_up[i][j] += dp_up[i - 1][j]
                if j > 0:
                    dp_left[i][j] += dp_left[i][j - 1]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 'W':
                    dp_down[i][j] = 0
                    dp_right[i][j] = 0
                    continue
                if grid[i][j] == 'E':
                    dp_down[i][j] = 1
                    dp_right[i][j] = 1
                if i < m - 1:
                    dp_down[i][j] += dp_down[i + 1][j]
                if j < n - 1:
                    dp_right[i][j] += dp_right[i][j + 1]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    res = max(res, dp_up[i][j] + dp_right[i][j] + dp_left[i][j] + dp_down[i][j])

        return res


grid = ["0E00",
        "E0WE",
        "0E00"
        ]
s = Solution()
print(s.max_killed_enemies(grid))

