class Solution:
    def findLongestWord(self, s, dictionary):
        def sub(word):
            i = 0
            for c in s:
                if i < len(word) and word[i] == c: i += 1
            return i == len(word)
        ans = ""
        for w in dictionary:
            if sub(w) and (len(w) > len(ans) or (len(w)==len(ans) and w < ans)):
                ans = w
        return ans
