from typing import (
    List,
)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return []
        result = []
        used = [0 for i in range(len(nums))]
        self.dfs(nums, used, [], result)
        return result

    def dfs(self, nums, used, current, result):
        if len(nums) == len(current):
            return result.append(list(current))

        for i in range(len(nums)):
            if used[i]:
                continue
            current.append(nums[i])
            used[i] = 1
            self.dfs(nums, used, current, result)
            current.pop()
            used[i] = 0




s = Solution()
print(s.permute([1, 2, 3]))
