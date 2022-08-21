from typing import (
    List,
)


class Solution:
    """
    @param nums: the input array
    @param target: the target number
    @return: return the target pair
             we will sort your return value in output
    """

    def two_sum_v_i_i(self, nums: List[int], target: int) -> List[List[int]]:
        # write your code here
        n = len(nums)
        if (n == 0):
            return []
        left = 0
        right = 0
        for i in range(n):
            if (nums[i] > nums[right]):
                right = i
            if (nums[i] < nums[left]):
                left = i
        ans = []
        while (nums[left] < nums[right]):
            if (nums[left] + nums[right] < target):
                left = self.nextleft(left, nums)
                if left == -1:
                    break
            elif (nums[left] + nums[right] > target):
                right = self.nextright(right, nums)
                if right == -1:
                    break
            else:
                tmp = [left, right]
                if left > right:
                    tmp[0], tmp[1] = tmp[1], tmp[0]
                ans.append(tmp)
                left = self.nextleft(left, nums)
                if left == -1:
                    break
        return ans

    def nextleft(self, left, nums):
        n = len(nums)
        if (nums[left] < 0):
            for i in range(left - 1, -1, -1):
                if (nums[i] < 0):
                    return i
            for i in range(n):
                if (nums[i] >= 0):
                    return i
            return -1
        for i in range(left + 1, n):
            if (nums[i] >= 0):
                return i
        return -1
    def nextright(self, right, nums):
        n = len(nums)
        if (nums[right] > 0):
            for i in range(right - 1, -1, -1):
                if (nums[i] > 0):
                    return i
            for i in range(n):
                if (nums[i] <= 0):
                    return i
            return -1
        for i in range(right + 1, n):
            if (nums[i] <= 0):
                return i
        return -1

numbers = [0, -1, 2, -3, 4]
s = Solution()
print(s.two_sum_v_i_i(numbers, 1))
