# LC 269. Alien Dictionary | Hard | Uber, Google
from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words):
        adj = defaultdict(set)
        indeg = {c: 0 for w in words for c in w}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j]); indeg[w2[j]] += 1
                    break
        q = deque(c for c in indeg if indeg[c] == 0)
        res = []
        while q:
            c = q.popleft(); res.append(c)
            for nei in adj[c]:
                indeg[nei] -= 1
                if indeg[nei] == 0: q.append(nei)
        return ''.join(res) if len(res) == len(indeg) else ""
