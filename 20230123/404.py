from typing import (
    List,
)


class Solution:

    def subarray_sum_i_i(self, a: List[int], start: int, end: int) -> int:
        i, j = 0, 0
        n = len(a)
        sumarray = a[i]
        lessthan = 0
        while i < n and j < n:
            if sumarray < start:
                j += 1
                if j >= i:
                    lessthan += j - i
                if j < n:
                    sumarray += a[j]
            else:
                sumarray -= a[i]
                i += 1
        i, j = 0, 0
        greatthan = 0
        sumarray = a[i]
        while i < n and j < n:
            if sumarray > end:
                greatthan += n - j
                sumarray -= a[i]
                i += 1
            else:
                j += 1
                if j < n:
                    sumarray += a[j]
        return greatthan

    def subarray_sum_i_i_2(self, a: List[int], start: int, end: int) -> int:
        n = len(a)
        big_s, small_s = 0, 0
        big_e, small_e = 0, 0

        ans = []
        # ans = 0
        for i in range(n):
            small_e = max(small_e, i)
            big_e = max(big_e, i)
            while small_e < n and small_s + a[small_e] < start:
                small_s += a[small_e]
                small_e += 1
            while big_e < n and big_s + a[big_e] <= end:
                big_s += a[big_e]
                big_e += 1
            if big_e - small_e > 0:
                # ans.append((a[small_e], a[big_e]))
                # ans += big_e - small_e
                a1 = []
                for i in range(big_e - small_e):
                    s = small_e + i
                    if s == big_e:
                        continue
                    a1.append(a[s])
                    ans.append(a1.copy())
            if small_e > i:
                small_s -= a[i]
            if big_e > i:
                big_s -= a[i]
        return ans



s = Solution()
print(s.subarray_sum_i_i_2([1, 2, 3, 4], 9, 100))
# print(s.subarray_sum_i_i_2([1, 2, 3, 4, 5], 8, 20))
