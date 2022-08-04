from typing import (
    List,
)


class Solution:
    """
    @param nums: a list of integer
    @param target: an integer
    @return: nothing
    """

    def move_target(self, nums: List[int], target: int):
        # write your code here
        # left, right, result = 0, len(nums) - 1, [0] * len(nums)
        # while left <= len(nums) and right >= 0:
        #     if nums[right] == target:
        #         result[left] = nums[right]
        #         left = left + 1
        #         right = right - 1
        #     else:
        #         result[right + left] = nums[right]
        #         right = right - 1
        # for i in range(len(nums)):
        #     nums[i] = result[i]

        count = 0
        left, right = len(nums) - 1, len(nums) - 1

        while left >= 0:
            if nums[left] != target:
                nums[right] = nums[left]
                right -= 1
            else:
                count += 1
            left -= 1

        for i in range(count):
            nums[i] = target
        print(nums)

        # return result
a = [5, 1, 6, 1]
b = [2, 4, 2]
# a = [5, 3, 1, -1, 6]
# b = [4, 8, 1, 1]
s = Solution()
s.move_target(a, 1)