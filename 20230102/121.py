import collections
from typing import (
    List, Set,
)


class Solution:

    def find_ladders(self, start: str, end: str, dict: Set[str]) -> List[List[str]]:
        dict.add(end)
        dict.add(start)
        queue = collections.deque([end])
        distance = {end: 1}
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_word(word, dict):
                if next_word in distance:
                    continue
                queue.append(next_word)
                distance[next_word] = distance[word] + 1
        print(distance)
        # after this step, we have a distance dictionary
        result = []
        self.dfs(start, end, distance, dict, [start], result)
        return result

    def get_next_word(self, word, dict):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                next_str = left + char + right
                if next_str in dict:
                    words.append(next_str)
        return words

    def dfs(self, current, target, distance, dict, path, result):
        if current == target:
            result.append(list(path))
            return
        for word in self.get_next_word(current, dict):
            if distance[word] != distance[current] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, dict, path, result)
            path.pop()

s = Solution()
start = "hit"
end = "cog"
dict = set()
dict.add("hot")
dict.add("dot")
dict.add("dog")
dict.add("lot")
dict.add("log")
print(s.find_ladders(start, end, dict))
