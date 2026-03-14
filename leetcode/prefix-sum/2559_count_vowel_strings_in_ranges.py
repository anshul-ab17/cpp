class Solution:
    def vowelStrings(self, words, queries):
        pref = [0]

        for w in words:
            pref.append(pref[-1] + (w[0] in 'aeiou' and w[-1] in 'aeiou'))

        return [pref[r+1] - pref[l] for l, r in queries]
