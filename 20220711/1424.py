from typing import (
    List,
)


class Solution:
    """
    @param a:
    @return: the length of the longest mountain
    """

    def longest_mountain(self, a: List[int]) -> int:
        # write your code here
        # size, begin, end, top = 0, 0, 1, 0
        # while end < len(a):
        #     while end < len(a) and a[end - 1] < a[end]:
        #         if top != 1:
        #             top = -1
        #         end += 1
        #     while end < len(a) and a[end - 1] > a[end]:
        #         end += 1
        #         if top == -1:
        #             top = 1
        #     # value = a[end]
        #     if top == 1:
        #         size = max(end - begin, size)
        #     if end == len(a):
        #         return size
        #     begin += 1
        #     end = begin + 1
        # return size
        if not a or not len(a):
            return 0

        left, right = 0, 0

        res = 0
        while right < len(a):
            if right > 1 and a[right - 2] >= a[right - 1] and a[right - 1] < a[right]:
                left = right - 1
            elif right > 1 and a[right - 1] == a[right]:
                left = right
            right += 1
            res = max(res, right - left)

        return res


# a = [2, 1, 4, 7, 3, 2, 5, 4, 3, 2, 1, 0]
# a = [0, 1, 2, 3, 1]
# a = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
a = [1, 2, 1, 2, 1, 2, 3, 2, 1, 2, 3]
s = Solution()
print(s.longest_mountain(a))
