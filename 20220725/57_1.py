from typing import (
    List,
)


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """

    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        nums = sorted(numbers)
        results = []
        length = len(nums)
        for i in range(0, length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.find_two_sum(nums, i + 1, length - 1, -nums[i], results)
        return results

    def find_two_sum(self, nums, left, right, target, results):
        while left < right:
            if nums[left] + nums[right] == target:
                results.append([-target, nums[left], nums[right]])
                right -= 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1


numbers = [-1, 0, 1, 2, -1, -4]
numbers = [1, 0, -1, -1, -1, -1, 0, 1, 1, 1]
s = Solution()
print(s.three_sum(numbers))