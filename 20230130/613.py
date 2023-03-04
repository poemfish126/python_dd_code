from typing import (
    List,
)


class Solution:

    def highFive(self, results):
        u_hash = dict()
        for r in results:
            if r[0] not in u_hash:
                u_hash[r[0]] = []
            if len(u_hash[r[0]]) >= 5:
                if u_hash[r[0]][0] < r[1]:
                    u_hash[r[0]].append(r[1])
                    u_hash[r[0]].sort()

            else:
                u_hash[r[0]].append(r[1])
                u_hash[r[0]].sort()
        answer = dict()
        for id, scores in u_hash.items():
            answer[id] = sum(scores) / len(scores)

        return answer


s = Solution()
print(s.highFive([[1, 91], [1, 92], [2, 93], [2, 99], [2, 98], [2, 97], [1, 60], [1, 58], [2, 100], [1, 61]]))
print(s.highFive([[1, 90], [1, 90], [1, 91], [1, 93], [1, 90], [1, 90]]))
print(s.highFive([[1, 93], [1, 90], [1, 90]]))
