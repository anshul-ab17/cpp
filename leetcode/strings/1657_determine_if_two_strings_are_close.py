from collections import Counter
class Solution:
    def closeStrings(self, w1, w2):
        return set(w1) == set(w2) and sorted(Counter(w1).values()) == sorted(Counter(w2).values())
