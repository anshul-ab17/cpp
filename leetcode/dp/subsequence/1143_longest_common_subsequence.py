# LC 1143. Longest Common Subsequence | Medium
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                tmp = dp[j]
                dp[j] = prev + 1 if text1[i-1] == text2[j-1] else max(dp[j], dp[j-1])
                prev = tmp
        return dp[n]
