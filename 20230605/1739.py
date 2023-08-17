from typing import (
    List,
)

class Solution:

    def at_most_n_given_digit_set(self, D: List[str], N: int) -> int:
        S = str(N)
        K = len(S)
        dp = [0] * K + [1]
        # dp[i] = total number of valid integers if N was "N[i:]"

        for i in range(K-1, -1, -1):
            # Compute dp[i]

            for d in D:
                if d < S[i]:
                    dp[i] += len(D) ** (K-i-1)
                elif d == S[i]:
                    dp[i] += dp[i+1]

        return dp[0] + sum(len(D) ** i for i in range(1, K))

s = Solution()
print(s.at_most_n_given_digit_set(["1", "3", "5", "7"], 100))
