from collections import Counter
class Solution:
    def topKFrequent(self, words, k):
        cnt = Counter(words)
        return sorted(cnt, key=lambda w: (-cnt[w], w))[:k]
