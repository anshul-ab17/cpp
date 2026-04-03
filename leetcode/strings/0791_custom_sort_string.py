from collections import Counter
class Solution:
    def customSortString(self, order, s):
        cnt = Counter(s)
        ans = []
        for c in order:
            ans.append(c * cnt[c])
            cnt[c] = 0
        for c, f in cnt.items():
            ans.append(c * f)
        return ''.join(ans)
