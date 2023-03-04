from typing import (
    List,
)
from lintcode.ListNode import *


class Solution:

    def reverse(self, head: ListNode) -> ListNode:
        current = None
        while head:
            temp = head.next
            head.next = current
            current = head
            head = temp
        return current

    def reverse_from_to(self, start: ListNode, end: ListNode) -> ListNode:
        current = None
        while start != end:
            temp = start.next
            start.next = current
            current = start
            start = temp
        return current

s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4
# print(s.reverse(l1))
print(s.reverse_from_to(l1, l3))

