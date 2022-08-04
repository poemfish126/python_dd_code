from typing import (
    List,
)


class Solution:
    """
    @param str: the string
    @param dict: the dictionary
    @return: return words which  are subsequences of the string
    """

    def find_words(self, str: str, dict: List[str]) -> List[str]:
        # write your code here.
        result = []
        for word in dict:
            print(word)
            if self.is_subsequence(str, word):
                result.append(word)
        return result

    def is_subsequence(self, str: str, t:str) -> bool:
        i, j = 0, 0
        while i < len(str) and j < len(t):
            if str[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(t)


str = "nmownhiterer"
dict = ["nowhere", "monitor", "moniter"]
s = Solution()
print(s.find_words(str, dict))
["nowhere", "moniter"]
