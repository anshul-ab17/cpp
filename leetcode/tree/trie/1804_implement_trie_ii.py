# Trie with word and prefix counts.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_count = 0
        self.prefix_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
            node.prefix_count += 1
        node.word_count += 1

    def _find(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def countWordsEqualTo(self, word):
        node = self._find(word)
        return node.word_count if node else 0

    def countWordsStartingWith(self, prefix):
        node = self._find(prefix)
        return node.prefix_count if node else 0

    def erase(self, word):
        node = self.root
        path = [node]
        for ch in word:
            node = node.children[ch]
            path.append(node)
        node.word_count -= 1
        for n in path[1:]:
            n.prefix_count -= 1
