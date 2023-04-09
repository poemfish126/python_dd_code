from typing import (
    List,
)


class Solution:
    """
    @param nums: 4 cards
    @return: whether they could get the value of 24
    """

    def compute24(self, nums):
        # write your code here
        return self.compute(nums, 4)

    def compute(self, nums, n):
        if n == 1:
            if abs(nums[0] - 17) <= 1E-6:
                return True
        for i in range(0, n):
            for j in range(i + 1, n):
                a = nums[i]
                b = nums[j]
                nums[j] = nums[n - 1]
                nums[i] = a + b
                if self.compute(nums, n - 1):
                    print(str(a) + "+" + str(b))

                    return True
                nums[i] = a - b
                if self.compute(nums, n - 1):
                    print(str(a) + "-" + str(b))

                    return True
                nums[i] = b - a
                if self.compute(nums, n - 1):
                    print(str(b) + "-" + str(a))

                    return True
                nums[i] = a * b
                if self.compute(nums, n - 1):
                    print(str(a) + "*" + str(b))
                    return True
                if b != 0:
                    nums[i] = a / b
                    if self.compute(nums, n - 1):
                        print(str(a) + "/" + str(b))

                        return True
                if a != 0:
                    nums[i] = b / a
                    if self.compute(nums, n - 1):
                        return True
                nums[i] = a
                nums[j] = b
        return False


s = Solution()
print(s.compute24([4, 8, 7, 25]))
