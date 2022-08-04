import sys
from typing import (
    List,
)


class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trap_rain_water(self, heights: List[int]) -> int:
        left_max = []
        curt_max = -sys.maxsize
        for height in heights:
            curt_max = max(curt_max, height)
            left_max.append(curt_max)

        right_max = []
        curt_max = -sys.maxsize
        for height in reversed(heights):
            curt_max = max(curt_max, height)
            right_max.append(curt_max)

        right_max = right_max[::-1]
        volumn = []
        water = 0
        n = len(heights)
        for i in range(n):
            volumn.append((min(left_max[i], right_max[i]) - heights[i]))
            water += (min(left_max[i], right_max[i]) - heights[i])
        return water


    def trap_rain_water1(self, heights: List[int]) -> int:
        # write your code here
        if not heights or len(heights) < 3:
            return 0
        store, left_h, left_p, right_h, right_p, flag = 0, 0, 0, 0, 0, 0

        left_array = []
        right_array = []
        # storage left point
        for i in range(len(heights) - 1):
            if heights[i + 1] < heights[i]:
                if flag == 1:
                    left_array.append(i)
                    flag = 0
            elif heights[i + 1] > heights[i]:
                flag = 1
            # else:
            #     # del left_array[-1]
            #     left_array.append(i + 1)
        # storage right point
        for i in range(len(heights) - 1):
            if heights[i + 1] < heights[i]:
                if flag == 1:
                    right_array.append(i)
                    flag = 0
            elif heights[i + 1] > heights[i]:
                flag = 1
            # else:
            #     del left_array[-1]
            #     right_array.append(i - 1)

        # while right_p < len(heights):
        #     # check left
        #     if heights[left_p] == 0 or left_h <= heights[left_p]:
        #         left_h = heights[left_p]
        #         left_p += 1
        #         right_p += 1
        #         break
        #     # check right
        #     if heights[left_p] >= heights[right_p]:
        #         store += heights[left_p] - heights[right_p]
        #     else:
        #         left_p = right_p
        #     right_p += 1
        return store


a = [0, 1, 0, 2, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# a = [1, 0, 2]
s = Solution()
print(s.trap_rain_water(a))
