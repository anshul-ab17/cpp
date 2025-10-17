from collections import Counter

class Solution:
    def fourSumCount(self, A, B, C, D):
        mp = Counter(a + b for a in A for b in B)

        ans = 0

        for c in C:
            for d in D:
                ans += mp[-(c + d)]

        return ans
