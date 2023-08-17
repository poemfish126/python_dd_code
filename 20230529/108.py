import sys


class Solution:

    def min_cut(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        isPalin = self.is_palin(s)
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            f[i] = sys.maxsize
            for j in range(i):
                if isPalin[j][i - 1]:
                    f[i] = min(f[i], f[j] + 1)

        return f[n]

    def is_palin(self, s):
        n = len(s)
        fn = [[False] * n for _ in range(n)]
        for c in range(n):
            i = c
            j = c
            while i >= 0 and j < n and s[i] == s[j]:
                fn[i][j] = True
                i -= 1
                j += 1
        for c in range(n - 1):
            i = c
            j = c + 1
            while i >= 0 and j < n and s[i] == s[j]:
                fn[i][j] = True
                i -= 1
                j += 1
        return fn


s = Solution()
print(s.min_cut("abcbaaabaaaaaaaaa"))
