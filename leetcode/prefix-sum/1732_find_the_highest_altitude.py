class Solution:
    def largestAltitude(self, gain):
        alt = ans = 0
        for g in gain:
            alt += g
            ans = max(ans, alt)
        return ans
