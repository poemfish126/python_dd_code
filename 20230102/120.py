import collections
from typing import (
    List,
)


class Solution:

    def ladder_length(self, start, end, dict):
        dict.append(end)
        queue = collections.deque([start])
        distance = {start: 1}
        while queue:
            word = queue.popleft()
            if word == end:
                return distance[word]

            for next_word in self.get_next_word(word, dict):
                if next_word in distance:
                    continue
                queue.append(next_word)
                distance[next_word] = distance[word] + 1

        return 0

    def get_next_word(self, word, dict):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                next_word = left + char + right
                if next_word in dict:
                    words.append(next_word)
        return words


s = Solution()
start = "hit"
end = "cog"
dict = ["hot", "dot", "dog", "lot", "log"]
print(s.ladder_length(start, end, dict))
