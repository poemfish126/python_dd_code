from typing import (
    List,
)


class Solution:
    """
    @param nums: the array of integers
    @param target:
    @return: the starting and ending position
    """

    def search_range(self, nums: List[int], target: int) -> List[int]:
        # Write your code here.
        begin, stop = -1, -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            begin = start
        elif nums[end] == target:
            begin = end
        else:
            begin = -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        if nums[end] == target:
            stop = end
        elif nums[start] == target:
            stop = start
        else:
            begin = -1
        return [begin, stop]


nums = [5, 7, 7, 8, 8, 10]
target = 8
s = Solution()
print(s.search_range(nums, target))
