from typing import (
    List,
)


class Solution:

    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        nums = sorted(numbers)
        result = []
        length = len(nums)
        for i in range(length - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.find_two_sum(nums, result, i + 1, length - 1, -nums[i])
        return result

    def find_two_sum(self, nums, result, left, right, target):

        if not nums:
            return
        while left < right:
            current_value = nums[left] + nums[right]
            if current_value == target:
                result.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif current_value > target:
                right -= 1
            else:
                left += 1


numbers = [-1, 0, 1, 2, -1, -4]
# numbers = [1, 0, -1, -1, -1, -1, 0, 1, 1, 1]
s = Solution()
print(s.three_sum(numbers))
