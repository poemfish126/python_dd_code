from typing import (
    List,
)
from lintcode.LinkedNode import *


class LRUCache:

    def __init__(self, capacity):
        self.key_to_pre = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity

    def set(self, key, value):
        if key in self.key_to_pre:  # key exist
            self.kick(self.key_to_pre[key])
            self.key_to_pre[key].next.value = value
            return

        self.push_back(LinkedNode(key, value))  # not exist, put into the new node
        if len(self.key_to_pre) > self.capacity:
            self.pop_front()

    def get(self, key):
        if key not in self.key_to_pre:
            return -1

        prev = self.key_to_pre[key]
        current = prev.next
        self.kick(prev)
        return current.value

    def kick(self, prev):  # move the prev to the tail
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next
        self.key_to_pre[node.next.key] = prev
        node.next = None
        self.push_back(node)

    def pop_front(self):
        head = self.dummy.next
        del self.key_to_pre[head.key]
        self.dummy.next = head.next
        self.key_to_pre[head.next.key] = self.dummy

    def push_back(self, node):
        self.key_to_pre[node.key] = self.tail
        self.tail.next = node
        self.tail = node


c = LRUCache(2)
c.set(2, 1)
c.set(1, 1)
c.set(2, 4)
c.get(2)
c.set(4, 1)
c.get(1)
c.get(2)
print(c.key_to_pre)
