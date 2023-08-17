from typing import (
    List,
)


class Solution:

    def find_min_difference(self, timePoints: List[str]) -> int:
        timepoint_int = []
        for i in timePoints:
            timepoint_int.append(self.getMinutes(i))
        timepoint_int.sort()
        ans = float('inf')
        t0 = timepoint_int[0]
        prevalue = t0
        for i in range(1, len(timepoint_int)):
            current_dif = timepoint_int[i] - prevalue
            ans = min(ans, current_dif)
            prevalue = timepoint_int[i]
        ans = min(ans, t0 + 60 * 24 - prevalue)
        return ans

    def getMinutes(self, t: str):
        return ((ord(t[0]) - ord("0")) * 10 + ord(t[1]) - ord("0")) * 60 + (ord(t[3]) - ord("0")) * 10 + ord(
            t[4]) - ord("0")


timePoints = ["00:00", "23:59("]
s = Solution()
print(s.find_min_difference(timePoints))
