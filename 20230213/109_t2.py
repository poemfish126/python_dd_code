from typing import (
    List,
)


class Solution:
    def minimum_total(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        #  initial dp from 0,0 to i, j
        dp = [[0] * (i + 1) for i in range(n)]

        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
        for i in range(2, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]


        return min(dp[n - 1])


triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
triangle = [[-10]]
s = Solution()
print(s.minimum_total(triangle))
