from typing import (
    List,
)


class Solution:

    def two_sum2(self, nums: List[int], target: int) -> int:
        count = 0
        if not nums or len(nums) < 2:
            return count
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            current_value = nums[left] + nums[right]
            if current_value <= target:
                left += 1
            else:
                count += right - left
                right -= 1
        # how many number between left, right
        return count


s = Solution()
print(s.two_sum2([2, 7, 11, 15], 24))
print(s.two_sum2([1, 1, 1, 1], 1))
print(s.two_sum2([-1, -2, -3, -4, -5, -6, -100, -98, -111, -11], -111))
