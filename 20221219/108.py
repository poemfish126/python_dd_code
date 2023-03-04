from typing import (
    List,
)


class Solution:

    def minCut(self, s):
        n = len(s)
        f = []
        # n * n
        p = [[False for x in range(n)] for x in range(n)]
        for i in range(n + 1):
            for j in range(i, n):
                if (s[i] == s[j] and (j - i < 2 or p[i + 1][j] - 1)):
                    p[i][j] = True
                    f[i] = min(f[i], f[j + 1] + 1)
        return f[0]


s = Solution()
print(s.minCut("aabbbaac"))
