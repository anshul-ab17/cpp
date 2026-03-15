# LC 127. Word Ladder | Hard
from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet: return 0
        q = deque([(beginWord, 1)]); visited = {beginWord}
        while q:
            word, steps = q.popleft()
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word == endWord: return steps + 1
                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word); q.append((new_word, steps + 1))
        return 0
