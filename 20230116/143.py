from typing import (
List,
)

class Solution:

    def sort_colors2(self, colors: List[int], k: int):
        self.partition(colors, 0, len(colors) - 1, 1, k)
        return colors

    def partition(self, colors, i_from, i_to, c_from, c_to):
        if c_from == c_to or i_from == i_to:
            return

        color = (c_from + c_to) // 2
        left, right = i_from, i_to
        while left <= right:
            while left <= right and colors[left] <= color:
                left += 1
            while left <= right and colors[right] > color:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
        self.partition(colors, i_from, right, c_from, color)
        self.partition(colors, left, i_to, color + 1, c_to)


s = Solution()
print(s.sort_colors2([3, 6, 2, 1, 4, 3, 4, 2, 3], 4))

