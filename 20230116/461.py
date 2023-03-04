from typing import (
    List,
)


class Solution:

    def kthSmallest(self, k, nums):
        n = len(nums)
        return self.partition(nums, 0, n - 1, k - 1)

    def partition(self, nums, start, end, k):
        left, right = start, end
        pivot = nums[left]

        while left < right:
            while left < right and nums[left] < pivot:
                left += 1
            while left < right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if k < right:
            return self.partition(nums, start, right, k)

        if k >= left:
            return self.partition(nums, left, end, k)

        return nums[k]


s = Solution()
print(s.kthSmallest(4, [3, 4, 1, 2, 5]))
