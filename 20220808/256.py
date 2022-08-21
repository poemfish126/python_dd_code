from typing import (
    List,
)


class Solution:
    """
    @param on_hand: the expiry days of m units of creamer already in stock
    @param supplier: the expiry days of n units of creamer available for order
    @param demand: the maximum units of creamer employees will uses daily
    @return: the maximum units of creamer the manager can order without waste
    """

    def stock_lounge(self, on_hand: List[int], supplier: List[int], demand: int) -> int:
        # write your code here
        m = len(on_hand)
        n = len(supplier)
        onHand = sorted(on_hand)
        supplierSorted = sorted(supplier)
        for i in range(m):
            if onHand[i] < i // demand:
                return -1
        left = 0
        right = n
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.check(onHand, supplierSorted, demand, mid):
                left = mid
            else:
                right = mid - 1
        if self.check(onHand, supplierSorted, demand, right):
            return right
        else:
            return left

    def check(self, onHand, supplier, demand, order):
        m = len(onHand)
        n = len(supplier)
        onHnadIndex = 0
        supplierIndex = n - order
        for i in range(m + order):
            if supplierIndex < n and (onHnadIndex == m or supplier[supplierIndex] <= onHand[onHnadIndex]):
                if supplier[supplierIndex] < i // demand:
                    return 0
                supplierIndex += 1
            else:
                if onHand[onHnadIndex] < i // demand:
                    return 0
                onHnadIndex += 1
        return 1


on_hand = [0, 0, 2, 3, 3, 3]
supplier = [2, 0, 1, 3, 4]
demand = 2
s = Solution()
print(s.stock_lounge(on_hand, supplier, demand))
