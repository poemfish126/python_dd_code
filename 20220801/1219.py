from typing import (
    List,
)


class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """

    def find_radius(self, houses: List[int], heaters: List[int]) -> int:
        # Write your code here
        heaters.sort()
        ans = 0
        for house in houses:
            ans = max(ans, self.closestHeater(house, heaters))
        return ans

    def closestHeater(self, house: int, heaters: List[int]) -> int:
        start = 0
        end = len(heaters) - 1
        while start + 1 < end:
            m = start + (end - start) // 2
            if heaters[m] == house:
                return 0
            elif heaters[m] < house:
                start = m
            else:
                end = m
        return min(abs(house - heaters[start]), abs(heaters[end] - house))


houses = [1, 2, 3, 4]
heaters = [1, 4]
s = Solution()
print(s.find_radius(houses, heaters))
