from typing import (
    List,
)
import queue


class Solution:

    def time_to_flower_tree(self, father: List[int], time: List[int]) -> int:
        n = len(father)
        G = [[] for i in range(n)]
        for i in range(1, n, 1):
            G[father[i]].append(i)
        maxx = 0
        eq = queue.Queue()
        eq.put((0, 0))
        while (not eq.empty()):
            curnode, curtime = eq.get()
            maxx = max(curtime, maxx)
            for i in range(len(G[curnode])):
                v = G[curnode][i]
                eq.put((v, curtime + time[v]))
        return maxx


father_list = [-1, 0, 0, 1]
time_list = [-1, 3, 5, 3]
s = Solution()
print(s.time_to_flower_tree(father_list, time_list))
