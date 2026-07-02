# Reverse words + Trie.
class Solution:
    def minimumLengthEncoding(self, words):
        word_set = set(words)
        for word in words:
            for i in range(1, len(word)):
                word_set.discard(word[i:])

        return sum(len(w) + 1 for w in word_set)
