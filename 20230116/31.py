from typing import (
    List,
)


class Solution:

    def partition_array(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        while left < right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left


s = Solution()
print(s.partition_array([3, 2, 2, 1], 2))
print(s.partition_array([3, 2, 3, 3, 2, 1], 2))
print(s.partition_array([3, 2, 3, 3, 2, 1], -1))
print(s.partition_array([], 2))
