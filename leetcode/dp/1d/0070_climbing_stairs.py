# LC 70. Climbing Stairs | Easy
class Solution:
    # Brute force recursive - O(2^n)
    def climbStairs_brute(self, n):
        if n <= 2: return n
        return self.climbStairs_brute(n-1) + self.climbStairs_brute(n-2)

    # DP O(n) time O(1) space
    def climbStairs(self, n):
        a, b = 1, 1
        for _ in range(n - 1): a, b = b, a + b
        return b
