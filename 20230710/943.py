from typing import (
    List,
)
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = [0] * len(nums)
        self.array[0] = nums[0]

        for index in range(1, len(nums)):
            self.array[index] = self.array[index - 1] + nums[index]

    def sumRange(self, i, j):
        if i - 1 < 0:
            return self.array[j]
        else:
            return self.array[j] - self.array[i - 1]


nums = [-2, 0, 3, -5, 2, -1]
n = NumArray(nums)
print(n.sumRange(0, 2))
