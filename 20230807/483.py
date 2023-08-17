from typing import (
    List,
)
from lintcode.ListNode import *


class Solution:

    def to_array_list(self, head: ListNode) -> List[int]:
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next
        return l

l5 = ListNode(5)
l3 = ListNode(3, l5)
l1 = ListNode(1, l3)
s = Solution()
print(s.to_array_list(l1))