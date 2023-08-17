from typing import (
    List,
)
from sortedcontainers import SortedList


class Solution:

    def contains_nearby_almost_duplicate(self, nums: List[int], k: int, t: int) -> bool:
        window = SortedList()
        for i in range(len(nums)):
            if i > k:
                window.remove(nums[i - 1 - k])
            window.add(nums[i])
            idx = window.bisect_left(nums[i])
            if idx > 0 and abs(window[idx] - window[idx-1]) <= t:
                return True
            if idx < len(window) - 1 and abs(window[idx + 1] - window[idx]) <= t:
                return True
        return False


s = Solution()
print(s.contains_nearby_almost_duplicate([1, 2, 3, 1], 4, 0))
