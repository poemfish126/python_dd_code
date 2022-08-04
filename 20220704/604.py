from typing import (
    List,
)


# https://www.lintcode.com/problem/604/

class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def win_sum(self, nums: List[int], k: int) -> List[int]:
        # write your code here
        begin, end = 0, k
        result = []
        window_sum = 0
        if k == 0 or len(nums) == 0:
            return result
        for i in range(k):
            window_sum += nums[i]
        while end <= len(nums) and k <= len(nums):
            if begin != 0:
                window_sum = window_sum + nums[end - 1] - nums[begin - 1]
            result.append(window_sum)
            begin += 1
            end += 1
        print(result)
        return result


a = [1, 2, 7, 8, 5]
s = Solution()
s.win_sum(a, 3)
