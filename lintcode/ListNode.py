import collections


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current = self
        str_value = str(current.val)
        while current.next:
            current = current.next
            str_value = str_value + "->" + str(current.val)
        return str_value

    def __lt__(self, other):
        return self.val < other.val
