from collections import defaultdict
class Solution:
    def characterReplacement(self, s, k):
        cnt = defaultdict(int)
        l = maxf = ans = 0
        for r, ch in enumerate(s):
            cnt[ch] += 1
            maxf = max(maxf, cnt[ch])
            while (r - l + 1) - maxf > k:
                cnt[s[l]] -= 1; l += 1
            ans = max(ans, r - l + 1)
        return ans
