from typing import (
    List,
)


class Solution:

    def two_sum6(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        count, left, right = 0, 0, len(nums) - 1
        nums.sort()
        while left < right:
            if nums[left] + nums[right] == target:
                count += 1
                left += 1
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            if nums[left] + nums[right] > target:
                right -= 1
            if nums[left] + nums[right] < target:
                left += 1
        return count


s = Solution()
print(s.two_sum6([1, 1, 2, 45, 46, 46], 47))
print(s.two_sum6([7, 11, 11, 1, 2, 3, 4], 22))
