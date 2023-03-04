from typing import (
    List,
)
from lintcode.ListNode import *


class Solution:

    def mergeKlist(self, lists):
        if not lists:
            return None
        return self.mergeHelper(lists, 0, len(lists) - 1)

    def mergeHelper(self, lists, start, end):
        if start == end:
            return lists[start]
        mid = (start + end) // 2
        left = self.mergeHelper(lists, start, mid)
        right = self.mergeHelper(lists, mid + 1, end)
        return self.merge_two_list(left, right)

    def merge_two_list(self, head1, head2):
        tail = dummy = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
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
# print(s.merge_two_lists(l1, l5))
print(s.mergeKlist([l1, l5]))
