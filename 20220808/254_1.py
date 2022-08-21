class Solution:
    """
    @param n: An integer
    @return: The sum of a and b
    """

    def drop_eggs(self, n: int) -> int:
        # write your code here
        # start, end, step = 0, n, 0
        #
        # while start + 1 < end:
        #     mid = start + (end // 3)
        #     if mid < end:
        #         start = mid
        #         step += 1
        # step += n % 3
        # return step

        x = 1
        while x * (x + 1) // 2 < n:
            x <<= 1

        left, right = 1, x
        while left + 1 < right:
            mid = left + (right - left) // 2
            if mid * (mid + 1) // 2 >= n:
                right = mid
            else:
                left = mid
        return left if left * (left + 1) // 2 >= n else right


s = Solution()
print(s.drop_eggs(1000))
