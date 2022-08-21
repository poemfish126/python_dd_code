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
        left = right - 1

        # 两根指针从中间往两边扩展，依次找到最接近的 k 个数
        results = []
        for _ in range(k):
            if self.isLeftCloser(a, target, left, right):
                results.append(a[left])
                left -= 1
            else:
                results.append(a[right])
                right += 1

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

    def isLeftCloser(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target


A = [1, 2, 3]
target = 2
k = 3
s = Solution()
print(s.k_closest_numbers(A, target, k))
