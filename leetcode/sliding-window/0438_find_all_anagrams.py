# LC 438. Find All Anagrams in a String | Medium
from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s): return []
        pc, sc = Counter(p), Counter(s[:len(p)])
        res = [0] if sc == pc else []
        for i in range(len(p), len(s)):
            sc[s[i]] += 1
            sc[s[i - len(p)]] -= 1
            if sc[s[i - len(p)]] == 0: del sc[s[i - len(p)]]
            if sc == pc: res.append(i - len(p) + 1)
        return res
