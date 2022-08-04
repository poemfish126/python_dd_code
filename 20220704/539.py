from typing import (
    List,
)
# https://www.lintcode.com/problem/539/description?fromId=291&_from=collection

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def move_zeroes(self, nums: List[int]):
        # write your code here
        left, right = 0, 0
        while left < len(nums):
            print(nums)
            if nums[left] != 0:
                nums[right] = nums[left]
                right += 1
            left += 1
            print(nums)
        for i in range(left - right):
            nums[right + i] = 0
        print(nums)

a = [0, 1, 0, 3, 12]
b = [2, 4, 2]
# a = [5, 3, 1, -1, 6]
# b = [4, 8, 1, 1]
s = Solution()
s.move_zeroes(a)



