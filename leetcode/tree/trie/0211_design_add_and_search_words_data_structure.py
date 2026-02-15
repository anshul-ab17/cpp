class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for ch in word:
            cur = cur.children.setdefault(ch, TrieNode())
        cur.end = True

    def search(self, word):
        def dfs(i, node):
            if i == len(word):
                return node.end

            ch = word[i]
            if ch == '.':
                return any(dfs(i + 1, child) for child in node.children.values())

            return ch in node.children and dfs(i + 1, node.children[ch])

        return dfs(0, self.root)
