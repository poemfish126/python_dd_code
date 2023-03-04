from typing import (
    List,
)


class Solution:

    def partition(self, s):
        result = []
        self.dfs(s, [], result)
        print(len(result))
        return result

    def dfs(self, s, subset, result):
        if len(s) == 0:
            return result.append(list(subset))

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.is_palindrome(prefix):
                subset.append(prefix)
                self.dfs(s[i:], subset, result)
                subset.pop()

    def is_palindrome(self, s):
        return s == s[::-1]


s = Solution()
print(s.partition("aabbbaac"))
