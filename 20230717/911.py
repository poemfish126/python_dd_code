from typing import (
    List,
)


class Solution:

    def max_sub_array_len(self, nums: List[int], k: int) -> int:
        m = {}
        ans = 0
        m[k] = 0
        n = len(nums)
        sum1 = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            sum1[i] = sum1[i - 1] + nums[i - 1]
            if sum1[i] in m:
                ans = max(ans, i - m[sum1[i]])
            if sum1[i] + k not in m:
                m[sum1[i] + k] = i
        return ans


s = Solution()
# print(s.max_sub_array_len([1, -1, 5, -2, 3], 2))
print(s.max_sub_array_len([1, 2, 1, 3, -1, 1, 1, 1, 1, 1], 4))
