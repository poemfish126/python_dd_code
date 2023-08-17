class Solution:

    def is_invalid_parentheses(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if not stack:
                    return False
                if ch == ']' and stack[-1] != '[' or ch == ')' and stack[-1] != '(' or ch == '}' and stack[-1] != '{':
                    return False
                stack.pop()

        return not stack


s = Solution()
print(s.is_invalid_parentheses("[]{{[]}}"))


