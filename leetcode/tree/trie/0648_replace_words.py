class TrieNode:
    def __init__(self):
        self.c = {}
        self.end = False

class Solution:
    def replaceWords(self, dictionary, sentence):
        root = TrieNode()

        for w in dictionary:
            cur = root
            for ch in w:
                cur = cur.c.setdefault(ch, TrieNode())
            cur.end = True

        def find(word):
            cur = root
            ans = ""
            for ch in word:
                if ch not in cur.c:
                    return word
                ans += ch
                cur = cur.c[ch]
                if cur.end:
                    return ans
            return word

        return " ".join(find(w) for w in sentence.split())
