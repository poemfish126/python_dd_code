


"""
Definition of ListNode:
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        # write your code here
        if n == 1 and head.next is not None:
            return None
        begin = -1 * n
        start_node = head
        end_node = head
        while end_node.next:
            if begin >= 0:
                start_node = start_node.next
            end_node = end_node.next
            begin += 1
        if start_node.next:
            start_node.next = start_node.next.next
        return head

a = ListNode(5, None)
b = ListNode(4, a)
c = ListNode(3, b)
d = ListNode(2, c)
e = ListNode(1, d)
# a = [1, 2, 7, 8, 5]
s = Solution()
s.remove_nth_from_end(e, 2)
