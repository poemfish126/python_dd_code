from lintcode.RandomListNode import *

class Solution:

    def copyRandomList(self, head):
        self.copyNode(head)
        self.copyRandom(head)
        return self.split(head)

    def copyNode(self, head):

        nextNode = head
        while nextNode is not None:
            copy_node = RandomListNode(nextNode.val)
            copy_node.next = nextNode.next
            nextNode.next = copy_node
            nextNode = copy_node.next

    def copyRandom(self, head):
        nextNode = head
        while nextNode is not None:
            if nextNode.random:
                nextNode.next.random = nextNode.random.next
            nextNode = nextNode.next.next

    def split(self, head):
        nhead = RandomListNode(0)
        nhead.next = head.next
        nextNode = nhead.next
        while nextNode.next is not None:
            nextNode.next = nextNode.next.next
            nextNode = nextNode.next
        return nhead.next


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
