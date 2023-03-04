from typing import (
    List,
)

null_value = [-1, -1]


class Solution:

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return null_value
        left, right = 0, len(nums) - 1
        while left < right:
            current_value = nums[left] + nums[right]
            if current_value == target:
                return [left + 1, right + 1]
            if current_value > target:
                right -= 1
            if current_value < target:
                left += 1
        return null_value


s = Solution()
print(s.two_sum([1, 1, 2, 45, 46, 46], 47))
