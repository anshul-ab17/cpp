class Solution:
    def getSum(self, a, b):
        MASK = 0xffffffff
        while b:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        return a if a <= 0x7fffffff else ~(a ^ MASK)
