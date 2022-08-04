from typing import (
    List,
)

# https://www.lintcode.com/problem/767/description?fromId=291&_from=collection
class Solution:
    """
    @param nums: a integer array
    @return: nothing
    """

    def reverse_array(self, nums: List[int]):
        # write your code here
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            # left_value = nums[left]
            # nums[left] = nums[right]
            # nums[right] = left_value
            left += 1
            right -= 1
        print(nums)
        return nums


a = [-4, -1, 0, 3, 10]
s = Solution()
s.reverse_array(a)
