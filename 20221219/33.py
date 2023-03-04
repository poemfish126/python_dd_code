from typing import (
    List,
)


class Solution:
    def solve_n_queen(self, n: int) -> List[List[int]]:
        result = []
        visited = {
            'col': set(),
            'sum': set(),
            'diff': set()
        }
        self.dfs(n, [], visited, result)
        return result

    def dfs(self, n, permutation, visited, result):
        if n == len(permutation):
            result.append(self.draw(permutation))
            return
        row = len(permutation)
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
            visited['diff'].remove(row - col)
            permutation.pop()

    def is_valid(self, permutation, visited, col):
        row = len(permutation)
        if col in visited['col']:
            return False
        if row + col in visited['sum']:
            return False
        if (row - col) in visited['diff']:
            return False
        return True

    def draw(self, permutation):
        board = []
        row = len(permutation)
        for col in permutation:
            row_string = '|'.join(['Q' if c == col else '*' for c in range(row)])
            board.append(row_string)
        return board


s = Solution()
print(s.solve_n_queen(2))
