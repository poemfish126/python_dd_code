from typing import (
    List,
)
import heapq


class Heap:
    def __init__(self):
        self.minheap = []
        self.delete_set = set()

    def push(self, index, val):
        heapq.heappush(self.minheap, (val, index))

    def _lazy_deletion(self):
        while self.minheap and self.minheap[0][1] in self.delete_set:
            heapq.heappop(self.minheap)

    def top(self):
        self._lazy_deletion()
        return self.minheap[0]

    def pop(self):
        self._lazy_deletion()
        heapq.heappop(self.minheap)

    def delete(self, index):
        self.delete_set.add(index)

    def is_empty(self):
        return not bool(self.minheap)


class Solution:

    def shortest_subarray(self, nums: List[int], k: int) -> int:
        prefix_sum = self.get_prefix_sum(nums)
        start, end = 1, len(nums)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_valid(prefix_sum, k, mid):
                end = mid
            else:
                start = mid
        if self.is_valid(prefix_sum, k, start):
            return start
        if self.is_valid(prefix_sum, k, end):
            return end
        return -1

    # def is_valid(self, prefix_sum, k, length):
    #     minheap = []
    #     for end in range(len(prefix_sum)):
    #         index = end - length - 1
    #         heapq.
    #         minheap.delete(index)
    #         if len(minheap) > 0 and prefix_sum[end] - minheap.top()[0] >= k:
    #             return True
    #         heapq.heappush(minheap, (prefix_sum[end], end))
    #     return False

    def is_valid(self, prefix_sum, k, length):
        minheap = Heap()
        for end in range(len(prefix_sum)):
            index = end - length - 1
            minheap.delete(index)
            if not minheap.is_empty() and prefix_sum[end] - minheap.top()[0] >= k:
                return True
            minheap.push(end, prefix_sum[end])
        return False

    def get_prefix_sum(self, nums):
        p_sum = [0]
        for num in nums:
            p_sum.append(p_sum[-1] + num)
        return p_sum


s = Solution()
nums = [1, 1, -1, 1, 2, -3]
k = 3
print(s.shortest_subarray(nums, k))
# 4   -2  3   -4  5   -6
# 0   1   2   3   4   5
# X   Y   X   Y   X   Y
# X   Y   Y   Y   Y   Y
