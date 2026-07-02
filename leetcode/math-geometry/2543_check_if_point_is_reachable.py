# GCD observation: moves preserve gcd(x, y); reachable iff gcd(targetX, targetY) == 1.
from math import gcd

class Solution:
    def isReachable(self, targetX, targetY):
        return gcd(targetX, targetY) == 1
