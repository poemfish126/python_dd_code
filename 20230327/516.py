import sys
from typing import (
    List,
)


class Solution:

    def min_cost_i_i(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n, m = len(costs), len(costs[0])

        f_a = [[0 for _ in range(m)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            min1, min2 = -1, -1
            for k in range(m):
                if min1 == -1 or f_a[i - 1][k] < f_a[i - 1][min1]:
                    min2 = min1
                    min1 = k
                else:
                    if min2 == -1 or f_a[i - 1][k] < f_a[i - 1][min2]:
                        min2 = k

            for j in range(m):
                if j != min1:
                    f_a[i][j] = f_a[i - 1][min1] + costs[i - 1][j]
                else:
                    f_a[i][j] = f_a[i - 1][min2] + costs[i - 1][j]

        res = sys.maxsize
        for j in range(m):
            res = min(res, f_a[n][j])
        return res


c = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
s = Solution()
print(s.min_cost_i_i(c))
