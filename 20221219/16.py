from typing import (
    List,
)


class Solution:
    def permute_unique(self, nums: List[int]) -> List[List[int]]:
        results = []
        if nums is None:
            return results
        nums = sorted(nums)
        used = [0 for i in range(len(nums))]
        self.dfs(nums, used, [], results)
        return results

    def dfs(self, nums, used, current, results):
        if len(nums) == len(current):
            return results.append(list(current))
        for i in range(len(nums)):
            if used[i]:
                continue
            if (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            current.append(nums[i])
            used[i] = 1
            self.dfs(nums, used, current, results)
            current.pop()
            used[i] = 0


s = Solution()
print(s.permute_unique([2, 2, 2]))
