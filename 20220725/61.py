from typing import (
    List,
)

class Solution:
    """
    @param a: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def search_range(self, a: List[int], target: int) -> List[int]:
        # write your code here
        begin, stop = -1, -1
        if not a or a[0] > target or a[-1] < target:
            return [begin, stop]
        if a[0] == target and a[-1] == target:
            return [0, len(a) - 1]
        start, end = 0, len(a) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] > target:
                end = mid
            else:
                start = mid
        if a[start] < target and a[end] == target:
            stop = end
        elif a[start] == target and a[end] > target:
            stop = start
        start, end = 0, len(a) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] < target:
                start = mid
            else:
                end = mid
        if a[start] < target and a[end] == target:
            begin = end
        elif a[start] == target and a[end] > target:
            begin = start
        return [begin, stop]


array = [5, 7, 7, 8, 8, 10]
target = 8
s = Solution()
print(s.search_range(array, target))
