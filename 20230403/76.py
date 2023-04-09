from typing import (
    List,
)


class Solution:
    def longest_increasing_subsequece(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)







        # dp = [1] * n
        # pre = [-1] * n
        # for i in range(n):
        #     for j in range(i):
        #         if nums[j] < nums[i] and dp[i] < dp[j] + 1:
        #             dp[i] = dp[j] + 1
        #             pre[i] = j
        #
        # longest, last = 1, -1
        # for i in range(n):
        #     if dp[i] > longest:
        #         longest = dp[i]
        #         last = i
        # path = []
        # while last != -1:
        #     path.append(nums[last])
        #     last = pre[last]
        # print(path[::-1])
        # return longest


nums = [5, 4, 1, 2, 4, 5, 3]
nums = [4, 2, 4, 5, 3, 7]
s = Solution()
print(s.longest_increasing_subsequece(nums))
