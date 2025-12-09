class Solution:
    def numDistinct(self, s, t):
        dp = [0] * (len(t) + 1)
        dp[0] = 1

        for i in range(1, len(s) + 1):
            prev = 1
            for j in range(1, len(t) + 1):
                cur = dp[j]
                if s[i - 1] == t[j - 1]:
                    dp[j] += prev
                prev = cur

        return dp[-1]
