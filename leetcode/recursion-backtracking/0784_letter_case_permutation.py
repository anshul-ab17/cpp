class Solution:
    def letterCasePermutation(self, s):
        ans = [""]
        for ch in s:
            if ch.isalpha():
                ans = [x+c for x in ans for c in [ch.lower(), ch.upper()]]
            else:
                ans = [x+ch for x in ans]
        return ans
