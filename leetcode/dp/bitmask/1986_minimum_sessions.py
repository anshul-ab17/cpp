# LC 1986. Minimum Number of Work Sessions | Medium (Bitmask DP)
class Solution:
    def minSessions(self, tasks, sessionTime):
        n = len(tasks); total = 1 << n
        dp = [float('inf')] * total; dp[0] = 0
        sub_sum = [0] * total
        for mask in range(total):
            for i in range(n):
                if mask & (1 << i): sub_sum[mask] = sub_sum[mask ^ (1 << i)] + tasks[i]; break
        for mask in range(1, total):
            sub = mask
            while sub:
                if sub_sum[sub] <= sessionTime:
                    dp[mask] = min(dp[mask], dp[mask ^ sub] + 1)
                sub = (sub - 1) & mask
        return dp[total - 1]
