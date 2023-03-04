from typing import (
    List,
)
from lintcode.ListNode import *


class Solution:
    def reverse_k_group(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        nhead = ListNode(0)
        nhead.next = head
        start = nhead
        while start.next:
            end = start
            for i in range(k):
                end = end.next
                if end is None:
                    return nhead.next
            res = self.reverse(start.next, end)
            start.next = res[0]
            start = res[1]
        return nhead.next

    def reverse(self, start, end):
        new_head = ListNode(0)
        new_head.next = start
        while new_head.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = new_head.next
            new_head.next = tmp
        # current = None
        # while start != end:
        #     temp = start.next
        #     start.next = current
        #     current = start
        #     start = temp
        # current.next = start
        return [end, start]


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
l4.next = l5
l5.next = l6
print(l1)
print(s.reverse_k_group(l1, 2))
