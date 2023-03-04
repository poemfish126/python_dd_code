from typing import (
    List,
)

class Solution:

    def subarray_sum(self, nums: List[int]) -> List[int]:
        # presum
        prefix_hash = {0: -1}
        prefix_sum = 0
        result = []
        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum in prefix_hash:
                result.append(prefix_hash[prefix_sum] + 1)
                result.append(i)
                break
            prefix_hash[prefix_sum] = i
        return result



s = Solution()
print(s.subarray_sum([-3, 1, -4, 2, -3, 4]))
print(s.subarray_sum([-3, -3, 1, 2, 4]))
print(s.subarray_sum([-3, 1, 2, -3, 1, 2, 4]))
