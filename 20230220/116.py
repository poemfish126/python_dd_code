from typing import (
    List,
)


class Solution:

    def can_jump(self, a: List[int]) -> bool:
        n = len(a)
        if n <= 1:
            return True

        count = 0
        dp = [False] * n
        dp[0] = True
        for i in range(1, n):
            for j in range(i):
                count += 1
                if dp[j] and a[j] + j >= i:
                    dp[i] = True
                    break
            print(str(i) + ":" + str(dp))
        print("count:" + str(count))
        return dp[n - 1] == 1


A = [2, 3, 1, 1, 4]
A = [3, 2, 1, 0, 4, 9, 9, 9, 9, 9, 9, 9, 9, 9]
# A = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
# A = [3, 2, 1, 0, 4]
# A = [1, 0]
s = Solution()
print(s.can_jump(A))
