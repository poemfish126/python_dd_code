class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """

    def longest_palindrome(self, s: str) -> str:
        # write your code here
        if not s:
            return ""
        longest = ''
        for middle in range(len(s)):
            # two middle
            pali = self.find_palindrome(middle, middle, s)
            if len(pali) > len(longest):
                longest = pali

            pali = self.find_palindrome(middle, middle + 1, s)
            if len(pali) > len(longest):
                longest = pali
        return longest

    def find_palindrome(self, left, right, s):
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        return s[left + 1:right]



a = "abcdzdcab"
s = Solution()
print(s.longest_palindrome(a))
