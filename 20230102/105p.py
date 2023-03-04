from lintcode.RandomListNode import *

class Solution:

    def copyRandomList(self, head):
        if head is None: return None
        nhead = RandomListNode(head.val)
        listMap = {}
        listMap[head] = nhead
        p = head
        q = nhead
        while p != None:
            q.random = p.random
            if p.next:
                q.next = RandomListNode(p.next.val)
                listMap[p.next] = q.next
            else:
                q.next = None
            p = p.next
            q = q.next

        # copy random node
        q = nhead
        while q:
            if q.random:
                q.random = listMap[q.random]
            q = q.next
        return nhead



s = Solution()
l1 = RandomListNode(1)
l2 = RandomListNode(2)
l3 = RandomListNode(3)
l4 = RandomListNode(4)
l5 = RandomListNode(5)
l6 = RandomListNode(6)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l1.random = l3
l2.random = l2
l3.random = l5
print(s.copyRandomList(l1))
