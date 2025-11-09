# LC 843. Guess the Word | Hard | Google
class Solution:
    def findSecretWord(self, words, master):
        import random
        def matches(a, b): return sum(x == y for x, y in zip(a, b))
        for _ in range(10):
            guess = random.choice(words)
            res = master.guess(guess)
            if res == 6: return
            words = [w for w in words if matches(w, guess) == res]
