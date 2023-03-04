from typing import (
    List,
)


class Solution:
    def combination_sum2(self, num: List[int], target: int) -> List[List[int]]:
        result = []
        subset = sorted(list(num))
        self.dfs(subset, 0, target, [], result)
        return result


    def dfs(self, subset, start_index, target, combination, result):
        if target < 0:
            return
        if target == 0:
            return result.append(list(combination))

        for i in range(start_index, len(subset)):
            if i > start_index and subset[i] == subset[i -1]:
                continue

            combination.append(subset[i])
            self.dfs(subset, i + 1, target - subset[i], combination, result)
            combination.pop()


s = Solution()
candidates = [7, 1, 2, 5, 1, 6, 10]
print(s.combination_sum2(candidates, 8))
