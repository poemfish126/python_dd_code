from lintcode.ListNode import *


class Solution:

    def count_nodes(self, head: ListNode) -> int:
        count = 0
        while head is not None:
            head = head.next
            count += 1
        return count


l5 = ListNode(5)
l3 = ListNode(3, l5)
l1 = ListNode(1, l3)
s = Solution()
print(s.count_nodes(l1))
