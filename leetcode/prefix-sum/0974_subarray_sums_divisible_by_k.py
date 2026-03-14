from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums, k):
        cnt = defaultdict(int)
        cnt[0] = 1

        pref = ans = 0
        for n in nums:
            pref = (pref + n) % k
            ans += cnt[pref]
            cnt[pref] += 1

        return ans
