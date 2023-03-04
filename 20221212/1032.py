import collections
from typing import (
    List,
)


class Solution:
    def letter_case_permutation(self, s: str) -> List[str]:
        visited = set()
        visited.add(s)
        queue = collections.deque([s])
        while queue:
            x = queue.popleft()
            for new in self.get(x):
                if new not in visited:
                    print("not in " + new)
                    visited.add(new)
                    queue.append(new)

        return list(visited)

    def get(self, s: str):
        for i in range(len(s)):
            ch = s[i]
            chu = ch.upper() if ch.islower() else ch.lower()
            if ch != chu:
                print("yield " + s[0:  i] + chu + s[i + 1:])
                yield s[0:  i] + chu + s[i + 1:]


s = Solution()
print(s.letter_case_permutation("a1b2d4e5"))
