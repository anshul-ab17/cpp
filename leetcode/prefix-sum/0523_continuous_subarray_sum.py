class Solution:
    def checkSubarraySum(self, nums, k):
        mp = {0: -1}
        pref = 0

        for i, n in enumerate(nums):
            pref = (pref + n) % k

            if pref in mp:
                if i - mp[pref] > 1:
                    return True
            else:
                mp[pref] = i

        return False
