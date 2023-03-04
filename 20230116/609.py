from typing import (
    List,
)


class Solution:

    def two_sum5(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            current = nums[left] + nums[right]
            if current <= target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count


s = Solution()
print(s.two_sum5([2, 7, 11, 15], 24))
