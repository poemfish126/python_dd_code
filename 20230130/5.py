from typing import (
    List,
)


class Solution:
    def kth_largest_element(self, k: int, nums: List[int]) -> int:
        n = len(nums)
        return self.partition(nums, 0, n - 1, n - k)

    def partition(self, nums, start, end, k):
        if start == end:
            return nums[k]
        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if right >= k:
            return self.partition(nums, start, right, k)
        if left <= k:
            return self.partition(nums, left, end, k)
        return nums[k]


s = Solution()
print(s.kth_largest_element(4, [3, 4, 1, 2, 5, 6, 12, 9, 999, -10]))
