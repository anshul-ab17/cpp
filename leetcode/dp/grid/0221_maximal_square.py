# LC 221. Maximal Square | Medium
class Solution:
    def maximalSquare(self, matrix):
        m, n = len(matrix), len(matrix[0]); mx = 0
        dp = [0] * (n + 1)
        for i in range(m):
            new_dp = [0] * (n + 1)
            for j in range(1, n + 1):
                if matrix[i][j-1] == '1':
                    new_dp[j] = min(dp[j], dp[j-1], new_dp[j-1]) + 1
                    mx = max(mx, new_dp[j])
            dp = new_dp
        return mx * mx
