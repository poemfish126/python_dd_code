import collections


class RandomListNode:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

    def __str__(self):
        current = self

        random_str = ""
        if current.random is not None:
            random_str = "(" + str(current.random.val) + ")"
        else:
            random_str = "(N)"

        str_value = str(current.val) + random_str
        while current.next:
            current = current.next
            if current.random is not None:
                random_str = "(" + str(current.random.val) + ")"
            else:
                random_str = "(N)"
            str_value = str_value + "->" + str(current.val) + random_str
        return str_value
