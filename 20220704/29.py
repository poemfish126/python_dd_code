from typing import (
    List,
)


class Solution:
    """
    @param a: sorted integer array A
    @param b: sorted integer array B
    @return: A new sorted integer array
    """

    def merge_sorted_array(self, a: List[int], b: List[int]) -> List[int]:
        # write your code here
        result = []
        if not a:
            return b
        if not b:
            return a

        left, right, current = 0, 0, 0
        while left < len(a) and right < len(b):
            if a[left] > b[right]:
                result.append(b[right])
                current += 1
                right += 1
            else:
                result.append(a[left])
                current += 1
                left += 1
        while left < len(a):
            result.append(a[left])
            left += 1
        while right < len(b):
            result.append(b[right])
            right += 1

        return result


A = [1, 2, 3, 4]
B = [2, 4, 5, 6]
s = Solution()
print(s.merge_sorted_array(A, B))
