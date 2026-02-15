# LC 338. Counting Bits | Easy
class Solution:
    def countBits_brute(self, n): return [bin(i).count('1') for i in range(n+1)]
    # DP - O(n)
    def countBits(self, n):
        dp = [0] * (n + 1)
        for i in range(1, n + 1): dp[i] = dp[i >> 1] + (i & 1)
        return dp
