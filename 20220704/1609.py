"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: the head node
    @return: the middle node
    """
    def middle_node(self, head: ListNode) -> ListNode:
        # write your code here.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        #
        # num = 0
        # node = head
        # while node.next is not None:
        #     num += 1
        #     node = node.next
        # middle = round((num + 1) / 2)
        # print(middle)
        # num, node = 0, head
        # while num < middle:
        #     node = node.next
        #     num += 1
        # return node


a = ListNode(5, None)
b = ListNode(4, a)
c = ListNode(3, b)
d = ListNode(2, c)
e = ListNode(1, d)
# a = [1, 2, 7, 8, 5]
s = Solution()
s.middle_node(e)
