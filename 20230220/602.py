from typing import (
    List,
)


class Solution:

    def max_envelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        oe = sorted(envelopes)
        dp = [1] * n
        pre = [-1] * n
        for i in range(n):
            for j in range(i):
                if oe[i][0] > oe[j][0] and oe[i][1] > oe[j][1] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    pre[i] = j
        max_v, last = 1, -1
        for i in range(n):
            if dp[i] > max_v:
                max_v = dp[i]
                last = i
        path = []
        while last != -1:
            path.append(oe[last])
            last = pre[last]
        print(path[::-1])
        return max_v


a = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
a = [[5, 4], [6, 4], [6, 7], [2, 3]]
s = Solution()
print(s.max_envelopes(a))
