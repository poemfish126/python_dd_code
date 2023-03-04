from typing import (
    List,
)


class Solution:

    def mergeSortedArray(self, A, m, B, n):
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 < 0:
                A[tail] = B[p2]
                p2 -= 1
            elif p2 < 0:
                A[tail] = A[p1]
                p1 -= 1
            elif A[p1] > B[p2]:
                A[tail] = A[p1]
                p1 -= 1
            else:
                A[tail] = B[p2]
                p2 -= 1
            tail -= 1
        return A


A = [0, 0, 0, 0, 0]
B = [1, 2, 4, 3, 5]
s = Solution()
print(s.mergeSortedArray(A, 0, B, 5))
