import heapq


class Solution:

    def topk(self, nums, k):
        heapq.heapify(nums)
        topk = heapq.nlargest(k, nums)
        topk.sort()
        topk.reverse()
        return topk


s = Solution()
print(s.topk([3, 10, 1000, -99, 4, 100], 3))
