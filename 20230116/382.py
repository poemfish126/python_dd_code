from typing import (
    List,
)


class Solution:

    def triangle_count(self, s: List[int]) -> int:
        count = 0
        if not s or len(s) < 3:
            return count
        nums = sorted(s)
        for i in range(len(nums) - 1, 0, -1):
            count += self.find_two_sum_greater(nums, 0, i - 1, nums[i])
        return count

    def find_two_sum_greater(self, nums, left, right, target):
        count = 0
        while left < right:
            current = nums[left] + nums[right]
            if current > target:
                count += right - left
                right -= 1
            else:
                left += 1
        return count


s = Solution()
print(s.triangle_count([3, 4, 6, 7]))
print(s.triangle_count([4, 4, 4, 4]))


