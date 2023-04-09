from typing import (
    List,
)


class Solution:

    def longest_increasing_c_subseq(self, a: List[int]) -> int:
        n = len(a)
        if n < 1:
            return 0
        if n < 2:
            return 1
        dp1, dp2 = 1, 1
        glomax = 0
        max_index = [0, 0]
        for i in range(1, n):
            if a[i] > a[i - 1]:
                dp1 += 1
                dp2 = 1
            elif a[i] < a[i - 1]:
                dp2 += 1
                dp1 = 1
            max_value = max(dp1, dp2)
            if glomax < max_value:
                glomax = max_value
                max_index[0] = i + 1
                max_index[1] = i - max_value + 1

            glomax = max(glomax, max(dp1, dp2))
        print(a[max_index[1]:max_index[0]])
        return glomax


s = Solution()
print(s.longest_increasing_c_subseq([1, 5, 4, 3, 3, 2, 1, 3]))
