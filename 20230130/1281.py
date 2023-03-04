import collections
from typing import (
    List,
)
import heapq


class Solution:

    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = dict()
        ccc = collections.Counter(nums)
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        freq_dict_sorted = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        count_sorted = sorted(ccc.items(), key=lambda x: x[1], reverse=True)
        res = list()
        for i in range(k):
            res.append(count_sorted[i][0])
        return res


s = Solution()
print(s.top_k_frequent([1, 1, 1, 2, 2, 3], 2))
