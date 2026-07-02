# Advanced Trie with prefix#suffix keys.
class WordFilter:
    def __init__(self, words):
        self.trie = {}
        for index, word in enumerate(words):
            n = len(word)
            for i in range(n + 1):
                suffix = word[i:]
                key = suffix + '#' + word
                node = self.trie
                for ch in key:
                    node = node.setdefault(ch, {})
                    node['idx'] = index

    def f(self, prefix, suffix):
        key = suffix + '#' + prefix
        node = self.trie
        for ch in key:
            if ch not in node:
                return -1
            node = node[ch]
        return node.get('idx', -1)
