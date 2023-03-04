from typing import (
    List,
)


class Solution:

    def findMedianSortedArray(self, A, B):
        m, n = len(A), len(B)
        p1, p2 = 0, 0

        left, right = -1, -1
        for i in range((m + n) // 2 + 1):
            left = right
            # move p2
            if p1 >= len(A) or p2 < len(B) and A[p1] > B[p2]:
                right = B[p2]
                p2 += 1
            # move p1
            else:
                right = A[p1]
                p1 += 1
        if (m + n) % 2 == 1:
            return right
        return (left + right) / 2

print(13 // 2)
a = [1, 2, 3, 4, 5, 6]
B = [2, 3, 4, 5]
s = Solution()
print(s.findMedianSortedArray(a, B))
