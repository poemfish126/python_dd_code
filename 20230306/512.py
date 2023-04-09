class Solution:

    def num_decodings(self, s: str) -> int:

        if not s:
            return 0
        n = len(s)
        f = [0 for i in range(n + 1)]
        f[0] = 1
        for i in range(1, n + 1):
            if int(s[i - 1]) >= 1:
                f[i] += f[i - 1]
            if i > 1:
                j = 10 * int(s[i - 2]) + int(s[i - 1])
                if 26 >= j >= 10:
                    f[i] += f[i - 2]
        return f[n]


s = Solution()
print(s.num_decodings("12021212"))
