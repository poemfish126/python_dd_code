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
        if not a or k < 1:
            return None
        l = len(a)
        start, end, p = 0, l - 1, 0
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] > target:
                end = mid
            elif a[mid] < target:
                start = mid
            else:
                end = mid
        start_value = abs(target - a[start])
        end_value = abs(target - a[end])

        if start_value > end_value:
            p = end
        else:
            p = start
        result = []
        result.append(a[p])
        left, right, count = p - 1, p + 1, 1
        while count < k and left >= 0 and right <= l - 1:
            left_value = abs(target - a[left])
            right_value = abs(target - a[right])
            if left_value <= right_value:
                result.append(a[left])
                count += 1
                left -= 1
            else:
                result.append(a[right])
                count += 1
                right += 1
        if left < 0 and count < k:
            for i in range(k - count):
                result.append(a[right + i])
        if right >= l and count < k:
            for i in range(k - count):
                result.append(a[left - i])
        return result


A = [1, 4, 6, 8, 11, 32, 133]
A = [1, 2, 3]
A = [1, 4, 8, 12, 16, 28, 38]

target = 7
k = 3
s = Solution()
print(s.k_closest_numbers(A, 12, 4))
