# LC 740. Delete and Earn | Medium (State Management DP)
class Solution:
    def deleteAndEarn(self, nums):
        if not nums: return 0
        mx = max(nums); earn = [0]*(mx+1)
        for n in nums: earn[n] += n
        prev2, prev1 = 0, 0
        for i in range(mx+1): prev2, prev1 = prev1, max(prev1, prev2 + earn[i])
        return prev1
