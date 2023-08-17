from typing import (
    List,
)

class Solution:

    def min_sub_array(self, nums: List[int]) -> int:
        dp = [[nums[i], 0] for i in range(len(nums))]
        min_sum = nums[0]
        for i in range(1, len(nums)):
            dp[i][1] = dp[i][0] + min(dp[i - 1][1], 0)
            min_sum = min(min_sum, dp[i][1])
        return min_sum

s = Solution()
print(s.min_sub_array([1, -1, -2, 1]))
