class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])
        ans, end = 0, -float('inf')
        for s,e in pairs:
            if s > end:
                ans += 1
                end = e
        return ans
