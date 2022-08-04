from typing import (
    List,
)


class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """

    def three_sum_smaller(self, nums: List[int], target: int) -> int:
        # Write your code here

        count = 0
        left, middle, right = 0, 1, 2
        while right < len(nums) and left < len(nums) - 2:
            for i in range(right, len(nums)):
                for j in range(middle, i):
                    if nums[left] + nums[j] + nums[i] < target:
                        count += 1
                        print(str(left) + ':' + str(j) + ':' + str(i))
                        print(str(nums[left]) + ':' + str(nums[j]) + ':' + str(nums[i]))
            left += 1
            middle = left + 1
            right = middle + 1
        return count


a = [-2, 0, 1, 3]
s = Solution()
print(s.three_sum_smaller(a, 2))
