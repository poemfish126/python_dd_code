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
        positions = {i: [] for i in 'abcdefghijklmnopqrstuvwxyz'}
        for i in range(len(str)):
            positions[str[i]].append(i)
        print(positions)

        for word in dict:
            if self.is_subsequence(positions, word, str):
                result.append(word)
        return result

    def is_subsequence(self, positions: dict, word: str, str: str) -> bool:
        i, j = 0, 0
        while i < len(str) and j < len(word):
            i = self.find_next(positions[word[j]], i)
            if i == -1:
                break
            j += 1

        return j == len(word)


    def find_next(self, c_l: List, position: int) -> int:
        start, end = 0, len(c_l) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if c_l[mid] > position:
                end = mid
            else:
                start = mid + 1
        if c_l[start] >= position:
            return c_l[start]
        if c_l[end] >= position:
            return c_l[end]
        return -1


str = "nmownhiterer"
dict = ["nowhere", "monitor", "moniter"]
s = Solution()
print(s.find_words(str, dict))
["nowhere", "moniter"]
