# LC 198. House Robber | Medium
class Solution:
    def rob(self, nums):
        if not nums: return 0
        prev2, prev1 = 0, 0
        for n in nums: prev2, prev1 = prev1, max(prev1, prev2 + n)
        return prev1
