class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x: int) -> int:
        # write your code here
        start, end = 0, x
        while start + 1 < end:
            mid = (start + end) // 2
            if mid * mid > x:
                end = mid
            elif mid * mid < x:
                start = mid + 1
            else:
                return mid

        if start * start == x:
            return start
        if end * end == x:
            return end
        return -1


s = Solution()
print(s.sqrt(4187))
