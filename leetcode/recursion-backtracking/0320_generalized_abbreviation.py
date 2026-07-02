# DFS generate abbreviations.
class Solution:
    def generateAbbreviations(self, word):
        res = []
        n = len(word)

        def dfs(i, cur, count):
            if i == n:
                res.append(cur + (str(count) if count else ""))
                return
            dfs(i + 1, cur, count + 1)
            dfs(i + 1, cur + (str(count) if count else "") + word[i], 0)

        dfs(0, "", 0)
        return res
