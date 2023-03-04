from typing import (
    List,
)


class Solution:
    def topk(self, nums, k):

        self.quick_select(nums, 0, len(nums) - 1, k)
        res = nums[:k]
        res.sort(reverse=True)
        return res

    def quick_select(self, nums, left, right, k):
        if left == right:
            return

        pivot = nums[left]
        i, j = left, right
        while i <= j:
            while i <= j and nums[i] > pivot:
                i += 1
            while i <= j and nums[j] < pivot:
                j -= 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        if j - left + 1 >= k:
            self.quick_select(nums, left, j, k)
        if i - left + 1 <= k:
            self.quick_select(nums, i, right, k - (i - left))


s = Solution()
print(s.topk([3, 10, 1000, -99, 4, 100], 3))
