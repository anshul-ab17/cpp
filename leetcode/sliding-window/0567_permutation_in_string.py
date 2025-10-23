from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
        need = Counter(s1)
        win = Counter()
        l = 0
        for r, ch in enumerate(s2):
            win[ch] += 1
            if r - l + 1 > len(s1):
                win[s2[l]] -= 1
                if win[s2[l]] == 0: del win[s2[l]]
                l += 1
            if win == need: return True
        return False
