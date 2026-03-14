class Solution:
    def findMaxLength(self, nums):
        mp = {0: -1}
        pref = ans = 0

        for i, n in enumerate(nums):
            pref += 1 if n == 1 else -1

            if pref in mp:
                ans = max(ans, i - mp[pref])
            else:
                mp[pref] = i

        return ans
