from typing import (
    List,
)
from lintcode.Record import *
import heapq


class Solution:

    def hightFive(self, results):
        all_user_dict = dict()
        for result in results:
            if result[0] not in all_user_dict:
                all_user_dict[result[0]] = []
            heapq.heappush(all_user_dict[result[0]], result[1])
            if len(all_user_dict[result[0]]) > 5:
                heapq.heappop(all_user_dict[result[0]])

            answer = dict()
        for id, scores in all_user_dict.items():
            answer[id] = sum(scores) / len(scores)
        return answer


s = Solution()
print(s.hightFive([[1, 91], [1, 92], [2, 93], [2, 99], [2, 98], [2, 97], [1, 60], [1, 58], [2, 100], [1, 61]]))
