# LC 340. Longest Substring with At Most K Distinct Characters | Medium | Microsoft
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        from collections import defaultdict
        count = defaultdict(int); l = res = 0
        for r in range(len(s)):
            count[s[r]] += 1
            while len(count) > k:
                count[s[l]] -= 1
                if count[s[l]] == 0: del count[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res
