from lintcode.ListNode import *


class Solution:

    def reverse_between(self, head: ListNode, m: int, n: int) -> ListNode:
        nhead = ListNode(0)
        nhead.next = head
        start, end, p = nhead, nhead, 0
        while p < n:
            p += 1
            if p < m:
                start = start.next
            if p < n:
                end = end.next
        new_start = self.reverse(start.next, end.next)
        start.next = new_start
        # new_end.next = end.next
        return nhead.next

    def reverse(self, start, end):
        new_head = ListNode(0)
        new_head.next = start
        new_end = start
        while new_head.next != end:
            tmp = new_end.next
            new_end.next = tmp.next
            tmp.next = new_head.next
            new_head.next = tmp
        return new_head.next



s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)
l8 = ListNode(8)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
print(l1)
print(s.reverse_between(l1, 2, 7))
