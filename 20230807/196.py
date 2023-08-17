from typing import (
    List,
)


class Solution:
    def find_missing(self, nums: List[int]) -> int:
        numbers = sorted(nums)
        for i in range(numbers[-1]):
            if i != numbers[i]:
                return i
        return -1


s = Solution()
print(s.find_missing([0, 1, 3]))
