from typing import (
    List,
)


class Solution:

    def move_zeroes(self, nums: List[int]):
        if nums is None:
            return None
        l = len(nums)
        left, right = 0, 0
        while right < l:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return nums

nums = [0, 1, 0, 3, 12]
s = Solution()
print(s.move_zeroes(nums))
