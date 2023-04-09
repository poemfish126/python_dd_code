from typing import (
    List,
)

class Solution:

    def max_product(self, nums: List[int]) -> int:
        if not nums:
            return None

        g_max = prev_max = prev_min = nums[0]

        for num in nums[1:]:
            if num > 0:
                cur_max = max(num, prev_max * num)
                cur_min = min(num, prev_min * num)
            else:
                cur_max = max(num, prev_min * num)
                cur_min = min(num, prev_max * num)
            g_max = max(g_max, cur_max)
            prev_max, prev_min = cur_max, cur_min
        return g_max


s = Solution()
print(s.max_product([2, 3, -2, 4]))
