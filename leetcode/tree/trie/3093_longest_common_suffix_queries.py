# Reverse Trie: insert reversed words, track shortest/earliest match at each node.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1
        self.best_len = float('inf')

class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        root = TrieNode()

        overall_best = 0
        for i, w in enumerate(wordsContainer):
            if len(w) < len(wordsContainer[overall_best]):
                overall_best = i

        for i, w in enumerate(wordsContainer):
            node = root
            self._update(node, i, len(w))
            for ch in reversed(w):
                node = node.children.setdefault(ch, TrieNode())
                self._update(node, i, len(w))

        res = []
        for q in wordsQuery:
            node = root
            best_idx, best_len = node.best_idx, node.best_len
            for ch in reversed(q):
                if ch not in node.children:
                    break
                node = node.children[ch]
                best_idx, best_len = node.best_idx, node.best_len
            res.append(best_idx)

        return res

    def _update(self, node, idx, length):
        if length < node.best_len or (length == node.best_len and idx < node.best_idx):
            node.best_len = length
            node.best_idx = idx
