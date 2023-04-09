from typing import (
    List,
)


class Solution:

    def coin_change(self, coins: List[int], amount: int) -> int:
        max_value = amount + 1
        f_a = [max_value for i in range(amount + 1)]
        f_a[0] = 0
        for i in range(1, amount + 1):
            min_v = amount
            for c in coins:
                if i >= c:
                    min_v = min(min_v, f_a[i - c])
            f_a[i] = min_v + 1
        return f_a[amount]

    def f_min(self, x):
        if x == 0:
            return 0
        res = 100
        if x >= 2:
            res = min(res, self.f_min(x - 2) + 1)
        if x >= 5:
            res = min(res, self.f_min(x - 5) + 1)
        if x >= 7:
            res = min(res, self.f_min((x - 7) + 1))
        return res


s = Solution()
# print(s.f_min(27))
print(s.coin_change([7, 2, 5], 27))
