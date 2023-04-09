import sys
from typing import (
    List,
)


class Solution:

    def min_cost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0


        f_a = [[0 for i in range(3)] for j in range(len(costs) + 1)]
        for i in range(1, len(costs) + 1):
            for j in range(3):
                f_a[i][j] = sys.maxsize
                for k in range(3):
                    if j != k:
                        f_a[i][j] = min(f_a[i][j], f_a[i - 1][k] + costs[i - 1][j])
        return min(f_a[i][0], f_a[i][1], f_a[i][2])


c = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
s = Solution()
print(s.min_cost(c))
