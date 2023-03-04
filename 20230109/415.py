from typing import (
    List,
)

class Solution:
    def is_palindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalpha() and not s[start].isnumeric():
                start += 1
            while start < end and not s[end].isalpha() and not s[end].isnumeric():
                end -= 1
            if start < end and s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1

        return True

a = "A man, a plan, a canal: Panama"
s = Solution()
print(s.is_palindrome(a))
