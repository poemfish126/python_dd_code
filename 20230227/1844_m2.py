from typing import (
    List,
)


class Solution:

    def subarray_sum_equals_k_i_i(self, nums: List[int], k: int) -> int:
        prefix_sum = self.get_prefix_sum(nums)
        n = len(nums)
        max_value = 0
        # for start in range(n):
        #     for end in range(start + 1, n):
        #         sum = prefix_sum[end + 1] - prefix_sum[start]
        #         if sum == k:
        #             print(str(sum) + "=" + str(nums[start]) + " to " + str(nums[end]))
        #             min_value = min(min_value, end - start + 1)
        #             break
        sum2index = {0: 0}
        for end in range(n):
            # prefix_sum[end + 1] - prefix_sum[start] = k
            match_p_s = prefix_sum[end + 1] - k
            if match_p_s in sum2index:
                length = end + 1 - sum2index[match_p_s]
                max_value = max(max_value, length)
            if prefix_sum[end + 1] not in sum2index:
                sum2index[prefix_sum[end + 1]] = end + 1
        return max_value

    def get_prefix_sum(self, nums):
        sums = [0]
        for i in nums:
            sums.append(sums[-1] + i)
        return sums


s = Solution()
nums = [2, 1, -1, 4, 2, -3]
k = 3
print(s.subarray_sum_equals_k_i_i(nums, k))
