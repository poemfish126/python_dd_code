import sys


class Solution:

    def min_cut(self, s: str) -> int:
        n = len(s)
        isPalindrome = [[False] * n for _ in range(n)]
        cuts = [0] * (n + 1)
        for i in range(n + 1):
            cuts[i] = n - i
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or isPalindrome[i + 1][j - 1]):
                    isPalindrome[i][j] = True
                    cuts[i] = min(cuts[i], cuts[j + 1] + 1)
        return cuts[0] - 1

s = Solution()
print(s.min_cut("abcbaaabaaaaaaaaa"))
