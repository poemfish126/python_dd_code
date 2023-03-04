from typing import (
    List,
)
from lintcode.Point import *

DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]


class Solution:

    def num_islands2(self, n: int, m: int, operators: List[Point]) -> List[int]:
        grid = [[0 for i in range(m)] for j in range(n)]
        visited = set()
        result = []
        for p in operators:
            if self.is_valid(n, m, visited, p.x, p.y):
                grid[p.x][p.y] = 1
                visited.add((p.x, p.y))
                new_visited = set()
                island = 0
                for i in range(n):
                    for j in range(m):
                        if grid[i][j] and (i, j) not in new_visited:
                            self.bfs(grid, n, m, i, j, new_visited)
                            island += 1

                result.append(island)

        return result

    def bfs(self, grid, n, m, x, y, visited):
        queue = collections.deque([(x, y)])
        visited.add((x, y))
        while queue:
            nx, ny = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                next_x = nx + delta_x
                next_y = ny + delta_y
                if not self.is_valid(n, m, visited, next_x, next_y):
                    continue
                if not grid[next_x][next_y]:
                    continue
                visited.add((next_x, next_y))
                queue.append((next_x, next_y))

    def is_valid(self, n, m, visited, x, y):
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False

        return True


s = Solution()
A = [Point(1, 1), Point(0, 1), Point(3, 3), Point(3, 4)]
print(s.num_islands2(4, 5, A))
