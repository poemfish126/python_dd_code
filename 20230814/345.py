from typing import (
    List,
)


class Solution:

    def get_sum(self, arr: List[int]) -> List[int]:
        result = []
        sorted_arr = [(arr[i], i) for i in range(len(arr))]
        sorted_arr.sort()
        prefix_sum = [0] * len(arr)
        current_sum = 1

        for i in range(len(sorted_arr)):
            prefix_sum[i] = current_sum
            current_sum *= sorted_arr[i][0]
        index_prefixsum = [(sorted_arr[i][1], prefix_sum[i]) for i in range(len(sorted_arr))]
        index_prefixsum.sort()
        result = [index_prefixsum[i][1] for i in range(len(index_prefixsum))]

        return result


s = Solution()
print(s.get_sum([2, 4, 8, 3]))
