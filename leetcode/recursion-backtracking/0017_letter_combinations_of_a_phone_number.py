class Solution:
    def letterCombinations(self, digits):
        if not digits: return []
        mp = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans = []
        def dfs(i, s):
            if i == len(digits):
                ans.append(s); return
            for ch in mp[digits[i]]:
                dfs(i+1, s+ch)
        dfs(0, "")
        return ans
