from typing import (
    List,
)


class Solution:

    def minimum_size(self, nums: List[int], s: int) -> int:
        if not nums:
            return -1
        sum_n, j, n = 0, 0, len(nums)
        min_length = n + 1
        for i in range(n):
            while j < n and sum_n < s:
                sum_n += nums[j]
                j += 1
            if sum_n >= s:
                min_length = min(min_length, j - i)
            sum_n -= nums[i]
        if min_length > n:
            return -1
        return min_length


nums = [2, 3, 1, 2, 4, 3]
s = Solution()
print(s.minimum_size(nums, 7))
