from typing import (
    List,
)


class Solution:
    """
    @param a: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def k_closest_numbers(self, a: List[int], target: int, k: int) -> List[int]:
        # write your code here
        right = self.findUpperClosest(a, target)
        # print(a[right])
        left = right - 1

        results = []
        for _ in range(k):
            if left == -1:
                results.append(a[right])
                if right < len(a) - 1:
                    right += 1
            elif right >= len(a):
                results.append(a[left])
                if left > 0:
                    left -= 1
            elif a[right] - target < target - a[left]:
                results.append(a[right])
                if right < len(a):
                    right += 1
            else:
                results.append(a[left])
                if left >= 0:
                    left -= 1
        return results

    def findUpperClosest(self, A, target):
        # find the first number >= target in A
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid

        if A[start] >= target:
            return start

        if A[end] >= target:
            return end

        # 找不到的情况
        return len(A)


a = [1, 4, 6, 8]
a = [1, 4, 6, 10, 20]
s = Solution()
print(s.k_closest_numbers(a, 20, 4))
