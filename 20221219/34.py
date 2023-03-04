from typing import (
    List,
)

class Solution:
    def total_n_queen(self, n: int) -> int:
        result = []
        visited = {
            'col': set(),
            'sum': set(),
            'diff': set()
        }
        self.dfs(n, [], visited, result)
        return len(result)

    def dfs(self, n, permutation, visited, result):
        row = len(permutation)
        if n == row:
            result.append(list(permutation))
            return

        for col in range(n):
            if not self.is_valid(permutation, visited, col):
                continue
            permutation.append(col)
            visited['col'].add(col)
            visited['sum'].add(row + col)
            visited['diff'].add(row - col)
            self.dfs(n, permutation, visited, result)
            visited['col'].remove(col)
            visited['sum'].remove(row + col)
            visited['diff'].remove((row - col))
            permutation.pop()

    def is_valid(self, permutation, visited, col):
        row = len(permutation)
        if col in visited['col']:
            return False
        if row + col in visited['sum']:
            return False
        if row - col in visited['diff']:
            return False
        return True

s = Solution()
print(s.total_n_queen(2))



