class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def length_of_longest_substring(self, s: str) -> int:
        # write your code here
        if not s:
            return 0
        longest = 0
        sub_dict = {}
        begin, end = 0, 0
        while end < len(s):
            current_c = s[end]
            if not sub_dict.get(current_c):
                sub_dict[current_c] = True
                end += 1
                if end == len(s):
                    longest = max(longest, end - begin)
            else:
                longest = max(longest, end - begin)
                sub_dict[s[begin]] = False
                begin += 1
        return longest
        unique_chars = set([])
        # j = 0
        # n = len(s)
        # longest = 0
        # for i in range(n):
        #     while j < n and s[j] not in unique_chars:
        #         unique_chars.add(s[j])
        #         j += 1
        #     longest = max(longest, j - i)
        #     unique_chars.remove(s[i])
        #
        # return longest


a = "abcabcbb"
# a = "aab"
s = Solution()
print(s.length_of_longest_substring(a))
