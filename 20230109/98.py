from lintcode.ListNode import *


class Solution:

    def sort_list(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        middle = self.find_middle(head)
        right = self.sort_list(middle.next)
        middle.next = None
        left = self.sort_list(head)
        return self.merge(left, right)

    def find_middle(self, head):
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, head1, head2):
        new_head = ListNode(0)
        tmp = new_head
        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                tmp.next = head1
                tmp = head1
                head1 = head1.next
            else:
                tmp.next = head2
                tmp = head2
                head2 = head2.next
        if head1 is None:
            tmp.next = head2
        if head2 is None:
            tmp.next = head1
        return new_head.next


s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)
l1.next = l3
l2.next = l4
l3.next = l5
l4.next = l6
l5.next = l7
l7.next = l2
# l6.next = l7
# print(s.sort_list(l1))
l11 = ListNode(1)
l12 = ListNode(-1)
l11.next = l12
print(s.sort_list(l11))
