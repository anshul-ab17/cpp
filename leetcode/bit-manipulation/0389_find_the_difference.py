class Solution:
    def findTheDifference(self, s, t):
        ans = 0
        for ch in s + t:
            ans ^= ord(ch)
        return chr(ans)
