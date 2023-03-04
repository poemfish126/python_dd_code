from typing import (
    List,
)


class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        result = []
        coins = sorted(list(set(coins)))
        self.dfs(coins, 0, amount, [], result)
        return len(result)

    def dfs(self, subset, start_index, target, combination, result):
        if target < 0:
            return
        if target == 0:
            return result.append(list(combination))
        for i in range(start_index, len(subset)):
            combination.append(subset[i])
            self.dfs(subset, i, target - subset[i], combination, result)
            combination.pop()


s = Solution()
coins = [2, 3, 8]
print(s.change(8, coins))
