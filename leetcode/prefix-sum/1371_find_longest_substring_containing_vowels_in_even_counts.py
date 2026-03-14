class Solution:
    def findTheLongestSubstring(self, s):
        mp = {0: -1}
        mask = ans = 0

        for i, ch in enumerate(s):
            if ch in 'aeiou':
                mask ^= 1 << 'aeiou'.index(ch)

            if mask in mp:
                ans = max(ans, i - mp[mask])
            else:
                mp[mask] = i

        return ans
