# Math + LCM/GCD.
from math import gcd

class Solution:
    def mirrorReflection(self, p, q):
        lcm = p * q // gcd(p, q)
        m = lcm // p
        n = lcm // q

        if m % 2 == 1 and n % 2 == 1:
            return 1
        if m % 2 == 0 and n % 2 == 1:
            return 0
        return 2
