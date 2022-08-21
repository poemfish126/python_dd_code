class Solution:
    """
    @param n: an integer
    @param k: an integer
    @return: how many problem can you accept
    """

    def can_accept(self, n: int, k: int) -> int:
        # Write your code here
        if not 1 <= k <= 50:
            return 0
        if not 1 <= n <= (2 ** 61 - 1):
            return 0

        def sum_n(num, k):
            return (1 + num) * num * k // 2

        start, end = 0, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if sum_n(mid, k) < n:
                start = mid
            else:
                end = mid
        if sum_n(end, k) > n >= sum_n(start, k):
            return start
        elif sum_n(end, k) == n and end < n - 1:
            return end

        return 0


n = 2305843009213693952
k = 1
s = Solution()
print(s.can_accept(n, k))
