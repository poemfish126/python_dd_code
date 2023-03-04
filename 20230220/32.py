from typing import (
    List,
)


class Solution:

    def min_window(self, source: str, target: str) -> str:
        target_dic = {}
        for i in target:
            target_dic[i] = target_dic.get(i, 0) + 1
        right, n, found = 0, len(source), 0
        # targetUniqueChar = len(target_dic)
        dic = {}
        target_len = len(target_dic)
        min_length = n + 1
        min_str = ""
        for i in range(n):
            while right < n and found < target_len:
                current = source[right]
                if current in target_dic:
                    dic[current] = dic.get(current, 0) + 1
                    if dic[current] == target_dic[current]:
                        found += 1
                right += 1
            if right - i < min_length and found == target_len:
                min_length = right - i
                min_str = source[i:right]
            if source[i] in target_dic:
                if dic[source[i]] == target_dic[source[i]]:
                    found -= 1
                dic[source[i]] -= 1
        return min_str


s = Solution()
print(s.min_window("adobecodebanc", "abc"))
