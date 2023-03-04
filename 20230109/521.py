from typing import (
    List,
)


class Solution:

    def deduplication(self, nums: List[int]) -> int:
        if nums is None: return 0
        length = len(nums)
        if length == 1: return 1
        left, right = 0, 0
        dic = {}
        while right < length:
            if nums[right] not in dic:
                dic[nums[right]] = 1
                nums[left] = nums[right]
                left += 1

            right += 1
        # nums.sort()
        # left, right = 0, 1
        # # tmp = nums[left]
        # while right < length:
        #     if nums[left] != nums[right]:
        #         left += 1
        #         nums[left] = nums[right]
        #     right += 1
        return left


s = Solution()
nums = [1, 3, 1, 4, 4, 2]
print(s.deduplication(nums))
print(nums)
