from typing import (
List,
)
import heapq

class Solution:
    def kth_largest_e2(self, nums, k):
        heap = []
        # for num in nums:
        #     heapq.heappush(heap, num)
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        #
        # return heapq.heappop(heap)
        # heapq.heapify(nums)
        topk = heapq.nlargest(k, nums)
        # heapq.heapify(nums)
        return topk[-1]

s = Solution()
print(s.kth_largest_e2([9, 3, 2, 4, 8], 3))



