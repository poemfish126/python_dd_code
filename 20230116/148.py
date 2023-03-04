from typing import (
    List,
)


class Solution:
    # 3 point, left, index, right.

    def sort_colors(self, nums: List[int]):
        left, index, right = 0, 0, len(nums) - 1

        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            elif nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
            else:
                index += 1
        return nums


s = Solution()
print(s.sort_colors([2, 1, 0, 1, 2, 1, 1, 0, 0, 0, 0]))
