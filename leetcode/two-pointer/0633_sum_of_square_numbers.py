class Solution:
    def judgeSquareSum(self, c):
        l, r = 0, int(c**0.5)
        while l <= r:
            s = l*l + r*r
            if s == c: return True
            if s < c: l += 1
            else: r -= 1
        return False
