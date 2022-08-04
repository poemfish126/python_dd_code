from typing import (
    List,
)


class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        # write your code here
        # transform numbers to a sorted array with index
        if not numbers:
            return [-1, -1]
        nums = [
            (number, index)
            for index, number in enumerate(numbers)
        ]
        nums = sorted(nums)
        left, right = 0, len(numbers) - 1
        while left <= right:
            current_value = nums[left][0] + nums[right][0]
            if current_value == target:
                return sorted([nums[left][1], nums[right][1]])
            if current_value > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]


a = [1, 2, 13, 7, 8, 5]
s = Solution()
print(s.two_sum(a, 10))
