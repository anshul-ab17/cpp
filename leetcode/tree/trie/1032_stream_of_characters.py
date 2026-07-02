# Reverse Trie + streaming queries.
class StreamChecker:
    def __init__(self, words):
        self.root = {}
        for word in words:
            node = self.root
            for ch in reversed(word):
                node = node.setdefault(ch, {})
            node['end'] = True
        self.stream = []

    def query(self, letter):
        self.stream.append(letter)
        node = self.root
        for ch in reversed(self.stream):
            if ch not in node:
                return False
            node = node[ch]
            if node.get('end'):
                return True
        return False
