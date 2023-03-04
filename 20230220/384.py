from typing import (
    List,
)


class Solution:

    def length_of_longest_substring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        length, right, n = 0, 0, len(s)
        dic = set([])

        for i in range(n):
            while right < n and s[right] not in dic:
                dic.add(s[right])
                right += 1
            length = max(length, right - i)
            dic.remove(s[i])
        return length


s = Solution()
print(s.length_of_longest_substring("abcabcbb"))
