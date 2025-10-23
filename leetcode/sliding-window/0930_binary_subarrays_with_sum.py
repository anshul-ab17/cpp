from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums, goal):
        pref = defaultdict(int); pref[0] = 1
        s = ans = 0
        for n in nums:
            s += n
            ans += pref[s-goal]
            pref[s] += 1
        return ans
