from lintcode.ListNode import *


class Solution:

    def hasCycle(self, head):
        if head is None or head.next is None:
            return None
        slow = head
        fast = head.next
        while fast != slow:
            if fast.next is None or fast.next.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True


s = Solution()
l1 = ListNode(21)
l2 = ListNode(10)
l3 = ListNode(4)
l4 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l1
print(s.hasCycle(l1))
