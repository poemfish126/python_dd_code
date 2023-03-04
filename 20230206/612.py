from typing import (
    List,
)
# from lintcode import (
#     Point,
# )
from lintcode.Point import *

import heapq


class Solution:

    def k_closest(self, points: List[Point], origin: Point, k: int) -> List[Point]:
        self.heap = []
        for point in points:
            distance = self.getDistance(point, origin)
            heapq.heappush(self.heap, (-distance, -point.x, - point.y))
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        res = []
        while len(self.heap) > 0:
            _, x, y = heapq.heappop(self.heap)
            res.append(Point(-x, -y))
        res.reverse()
        return res

    def getDistance(self, a: Point, b: Point):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2


s = Solution()
print((-54, -3, -4) < (-9, -100, -1000))
print(s.k_closest([Point(4, 6), Point(4, 7), Point(4, 4), Point(2, 5), Point(1, 1)], Point(0, 0), 3))
