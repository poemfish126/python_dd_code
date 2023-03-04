from typing import (
    List,
)


class Solution:

    def two_sum_closest(self, nums: List[int], target: int) -> int:
        if not nums:
            return target
        nums = sorted(nums)
        left, right = 0, len(nums) - 1
        min_diff = 1 << 31
        while left < right:
            current_diff = nums[left] + nums[right] - target
            if current_diff == 0:
                return 0
            if abs(current_diff) < min_diff:
                min_diff = abs(current_diff)
            if current_diff < 0:
                left += 1
            if current_diff > 0:
                right -= 1
        return min_diff


s = Solution()
print(s.two_sum_closest([0, 1, 2], 0))
print(s.two_sum_closest([-1, 2, 1, -4], 4))
print(s.two_sum_closest([-1, -1, -1, -4], 4))
