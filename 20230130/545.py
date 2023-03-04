import heapq

class Solution:

    def __init__(self, k):
        self.k = k
        self.heap = []

    def add(self, num):
        heapq.heappush(self.heap, num)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def topk(self):
        return sorted(self.heap, reverse=True)

s = Solution(3);
s.add(3)
s.add(10)
s.topk()
s.add(1000)
s.add(-99)
s.topk()
s.add(4)
s.topk()
s.add(100)
s.topk()
