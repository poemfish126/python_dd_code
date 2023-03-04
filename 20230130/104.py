from typing import (
    List,
)
import heapq
from lintcode.ListNode import *

class Solution:

    def mergeKLists(self, lists):
        if not lists:
            return None
        dummy = ListNode(0)
        tail = dummy
        heap = []
        result = []
        for list in lists:
            if list:
                heapq.heappush(heap, list)

        while heap:
            small = heapq.heappop(heap)
            tail.next = small
            if small.next:
                heapq.heappush(heap, small.next)
            tail = small
        return dummy.next

s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l1.next = l2
l2.next = l3
l3.next = l4
# l4.next = l5
l5.next = l6
print(l1)
print(s.mergeKLists([l1, l5]))
