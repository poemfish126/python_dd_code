from typing import (
    List,
)


class Solution:
    def house_robber2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n <= 2:
            return max(nums)
        old, new = 0, nums[0]
        for i in range(2, n):
            t = max(new, old + nums[i - 1])
            old = new
            new = t
        no_last = new
        old, new = 0, nums[1]
        for i in range(3, n + 1):
            t = max(new, old + nums[i - 1])
            old = new
            new = t
        no_first = new
        return max(no_first, no_last)


a = [2, 3, 2, 3]
# a = [3, 6, 4]
s = Solution()
print(s.house_robber2(a))
