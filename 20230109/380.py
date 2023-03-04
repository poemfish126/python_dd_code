from lintcode.ListNode import *


class Solution:

    def getIntesectionNode(self, headA, headB):
        if headA is None or headB is None: return None
        seenA = set()
        while headA:
            seenA.add(headA)
            headA = headA.next

        while headB:
            if headB in seenA:
                return headB
            headB = headB.next

        return None


s = Solution()

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)
l8 = ListNode(8)
l9 = ListNode(9)
l10 = ListNode(10)
l11 = ListNode(11)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l7.next = l8
l8.next = l9
l9.next = l5

l6.next = l10
l10.next = l11
print(s.getIntesectionNode(l1, l7))
