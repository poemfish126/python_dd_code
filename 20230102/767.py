from typing import (
    List,
)


class Solution:
    def reserse_array(self, nums: List[int]):
        start = 0
        end = len(nums) - 1
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
        return nums


nums = [1, 2, 5]
s = Solution()
print(s.reserse_array(nums))c
