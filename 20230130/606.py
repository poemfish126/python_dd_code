from typing import (
    List,
)


class Solution:

    def kth_largest_e2(self, nums, k):
        n = len(nums)
        self.quick_select(nums, 0, n - 1, n - k)
        return nums[n - k]

    def quick_select(self, nums, start, end, k):
        if start == end:
            return
        pivot = nums[start]
        left, right = start, end

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if k <= right:
            self.quick_select(nums, start, right, k)
        if k >= left:
            self.quick_select(nums, left, end, k)


s = Solution()
print(s.kth_largest_e2([9, 3, 2, 4, 8, 8, 8, 8], 7))
