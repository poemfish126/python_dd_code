from typing import (
    List,
)


class Solution:

    def win_sum(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, k
        if nums is None or k > len(nums):
            return 0
        result = []
        group = 0
        for i in range(k):
            group += nums[i]
        result.append(group)
        while right < len(nums):
            group = group - nums[left] + nums[right]
            result.append(group)
            left += 1
            right += 1
        return result


s = Solution()
array = [1, 2, 7, 8, 5]
print(s.win_sum(array, 3))
