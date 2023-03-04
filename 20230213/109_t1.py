from typing import (
    List,
)


class Solution:
    def minimum_total(self, triangle: List[List[int]]) -> int:
        return self.divide_conquer(triangle, 0, 0, {})

    def divide_conquer(self, triangle, x, y, memo):
        if x == len(triangle):
            return 0
        if (x, y) in memo:
            return memo[(x, y)]

        left = self.divide_conquer(triangle, x + 1, y, memo)
        right = self.divide_conquer(triangle, x + 1, y + 1, memo)
        memo[(x, y)] = min(left, right) + triangle[x][y]
        return memo[(x, y)]


triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
triangle = [[-10]]
s = Solution()
print(s.minimum_total(triangle))
