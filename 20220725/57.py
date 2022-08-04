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
        # write your code here
        result = []
        if not numbers:
            return [-1, -1]
        nums = [
            (number, index)
            for index, number in enumerate(numbers)
        ]
        nums = sorted(nums)
        for i in range(len(nums)):
            sub_array = self.two_sum_skip(nums, nums[i])
            if sub_array:
                sub_array.append(nums[i][1])
                sorted_sub = sorted(sub_array)
                if len(result) == 0:
                    result.append(sorted_sub)
                else:
                    duplicate = False
                    for x in result:
                        total_same = True
                        for j in range(len(x)):
                            if x[j] != sorted_sub[j]:
                                total_same = False
                                break
                        if total_same:
                            duplicate = True
                    if not duplicate:
                        result.append(sorted_sub)
        final_result = []
        for sub in result:
            replace_sub = []
            for i in sub:
                replace_sub.append(numbers[i])
            final_result.append(sorted(replace_sub))
        return result

    def two_sum_skip(self, nums, skip) -> List[int]:
        # write your code here
        # transform numbers to a sorted array with index
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left][1] == skip[1] or left == right:
                left += 1
                continue
            elif nums[right][1] == skip[1]:
                right -= 1
                continue
            current_value = nums[left][0] + nums[right][0]
            if current_value == skip[0] * -1:
                return sorted([nums[left][1], nums[right][1]])
            if current_value > skip[0] * -1:
                right -= 1
            else:
                left += 1
        return None


numbers = [-1, 0, 1, 2, -1, -4]
numbers = [1, 0, -1, -1, -1, -1, 0, 1, 1, 1]
s = Solution()
print(s.three_sum(numbers))
