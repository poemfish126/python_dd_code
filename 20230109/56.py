from typing import (
    List,
)


class Solution:

    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [-1, -1]
        nums = [
            (number, index)
            for index, number in enumerate(numbers)
        ]
        left, right = 0, len(nums) - 1
        nums = sorted(nums)
        while left <= right:
            current = nums[left][0] + nums[right][0]
            if current == target:
                return sorted([nums[left][1], nums[right][1]])
            if current < target:
                left += 1
            if current > target:
                right -= 1
        return [-1, -1]


s = Solution()
numbers = [7, 2, 11, 15]
print(s.two_sum(numbers, 9))
numbers = [0, 4, 3, 0]
print(s.two_sum(numbers, 0))
