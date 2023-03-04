from typing import (
    List,
)
from lintcode.Interval import *


class Solution:

    def merge(self, intervals: List[Interval]) -> List[Interval]:
        intervals = sorted(intervals, key=lambda x: x.start)
        result = []
        for item in intervals:
            if len(result) == 0 or result[-1].end < item.start:
                result.append(item)
            else:
                result[-1].end = max(result[-1].end, item.end)
        return result



l = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]

s = Solution()
for i in s.merge(l):
    print(i)
