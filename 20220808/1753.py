from typing import (
    List,
)


class Solution:
    """
    @param cost: the cost
    @param val: the val
    @return: the all cost
    """

    def doing_homework(self, cost: List[int], val: List[int]) -> int:
        # Write your code here.
        total_cost = []
        total = 0
        for i in cost:
            total += i
            total_cost.append(total)
        print(total_cost)
        total = 0
        for i in val:
            total += self.find_max(total_cost, i)
        return total

    def find_max(self, total_cost: List[int], num: int) -> int:
        start, end = 0, len(total_cost) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if total_cost[mid] == num:
                return num
            elif total_cost[mid] < num:
                start = mid
            else:
                end = mid
        if total_cost[end] <= num:
            return total_cost[end]
        if total_cost[start] <= num:
            return total_cost[start]
        return 0


cost = [3, 7, 3, 2, 5]
cost = [1, 2, 3, 5]
val = [10, 20, 12, 8, 17, 25]
val = [6, 10, 4]
s = Solution()
print(s.doing_homework(cost, val))
