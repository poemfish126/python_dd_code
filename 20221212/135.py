from typing import (
    List,
)


class Solution:

    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        # sort candidates
        candidates = sorted(list(set(candidates)))

        self.dfs(candidates, 0, target, [], result)

        return result

    def dfs(self, subset, start_index, target, combination, result):
        if target < 0:
            return

        if target == 0:
            # deepcopy
            return result.append(list(combination))

        for i in range(start_index, len(subset)):
            combination.append(subset[i])
            self.dfs(subset, i, target - subset[i], combination, result)
            combination.pop()


s = Solution()
candidates = [1, 2, 3, 6, 7]
print(s.combination_sum(candidates, 7))
