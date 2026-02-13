# LC 191. Number of 1 Bits | Easy
class Solution:
    def hammingWeight_builtin(self, n): return bin(n).count('1')
    # Brian Kernighan
    def hammingWeight(self, n):
        count = 0
        while n: n &= n - 1; count += 1
        return count
