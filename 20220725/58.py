from typing import (
    List,
)


class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
             we will sort your return value in output
    """

    def four_sum(self, numbers: List[int], target: int) -> List[List[int]]:
        # write your code here
        if not numbers:
            return []

        nums = sorted(numbers)
        results = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                pairs = self.find_two_sum_pairs(
                    nums,
                    j + 1,
                    len(nums) - 1,
                    target - nums[i] - nums[j],
                )

                for (c, d) in pairs:
                    results.append([nums[i], nums[j], c, d])

        return results

    def find_two_sum_pairs(self, nums, left, right, target):
        pairs = []
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                if not pairs or (nums[left], nums[right]) != pairs[-1]:
                    pairs.append((nums[left], nums[right]))
                left += 1
                right -= 1
        return pairs


numbers = [1, 0, -1, 0, -2, 2]
s = Solution()
print(s.four_sum(numbers, 0))