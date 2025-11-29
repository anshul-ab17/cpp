# LC 76. Minimum Window Substring | Hard
from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not t or not s: return ""
        need = Counter(t)
        have, required = 0, len(need)
        res, res_len = [-1, -1], float('inf')
        l, window = 0, {}
        for r, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            if ch in need and window[ch] == need[ch]: have += 1
            while have == required:
                if (r - l + 1) < res_len:
                    res, res_len = [l, r], r - l + 1
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]: have -= 1
                l += 1
        return s[res[0]:res[1]+1] if res_len != float('inf') else ""
