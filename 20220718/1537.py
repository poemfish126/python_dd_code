from typing import (
    List,
)


class Solution:
    """
    @param nums: an Integer array
    @return: return the minimum number of swaps.
    """

    def swap_zero_one(self, nums: List[int]) -> int:
        # Write your code here
        if len(nums) <= 1:
            return 0
        step, begin, end = 0, 0, 1
        while begin < len(nums) and end < len(nums):
            if nums[begin] == 1 and nums[end] == 0:
                nums[begin], nums[end] = nums[end], nums[begin]
                step += 1
                if begin == 0:
                    begin += 1
                    end += 1
                else:
                    begin -= 1
                    end -= 1
            else:
                begin += 1
                end += 1
            # print(nums) and end == 1:
            # print(str(step) + ',' + str(begin) + ',' + str(end))
        return step
        # prefix = [0]
        # ans = 0
        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         prefix.append(prefix[-1] + 1)
        #     else:
        #         prefix.append(prefix[-1])
        #         ans += prefix[-1]
        #     print(nums)
        #     print(prefix)
        # return ans


a = [1, 0, 1, 1, 0, 0, 0, 1]
s = Solution()
print(s.swap_zero_one(a))
