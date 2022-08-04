from typing import (List, )


class Solution:

    def minimal_distance(self, a: List[int], b: List[int]) -> List[int]:
        ans = b
        n = len(a)
        m = len(b)
        a.sort()
        for i in range(m):
            id = self.lowerBound(a, b[i])
            if (id == 0):
                ans[i] = a[id]
            elif (id == n):
                ans[i] = a[id - 1]
            else:
                if (b[i] - a[id - 1] <= a[id] - b[i]):
                    ans[i] = a[id - 1]
                else:
                    ans[i] = a[id]
        print(ans)
        return ans
        #
        # result = []
        # for i in b:
        #     min_distance = 1000
        #     min_number = 1000
        #     for j in a:
        #         distance = abs(i - j)
        #         if min_distance > distance:
        #             min_distance = distance
        #             min_number = j
        #         if min_distance == distance and min_number > j:
        #             min_number = j
        #     result.append(min_number)
        # print(result)

    def lowerBound(self, a, val):
        l = 0
        r = len(a)
        while (r - l > 1):
            mid = int((l + r) / 2)
            if (a[mid] >= val):
                r = mid
            else:
                l = mid
        if (a[l] >= val):
            return l
        else:
            return r



a = [5, 1, 2, 3]
b = [2, 4, 2]
# a = [5, 3, 1, -1, 6]
# b = [4, 8, 1, 1]
s = Solution()
s.minimal_distance(a, b)
