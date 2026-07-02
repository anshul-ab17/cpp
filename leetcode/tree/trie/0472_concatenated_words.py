# Trie + DFS / DP.
class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        word_set = set(words)
        memo = {}

        def can_form(word):
            if word in memo:
                return memo[word]
            for i in range(1, len(word)):
                prefix, suffix = word[:i], word[i:]
                if prefix in word_set and (suffix in word_set or can_form(suffix)):
                    memo[word] = True
                    return True
            memo[word] = False
            return False

        res = []
        for word in words:
            if not word:
                continue
            word_set.discard(word)
            if can_form(word):
                res.append(word)
            word_set.add(word)

        return res
