# LC 202. Happy Number | Easy
class Solution:
    # Floyd's cycle detection
    def isHappy(self, n):
        def nxt(x):
            s = 0
            while x: x, d = divmod(x, 10); s += d * d
            return s
        slow, fast = n, nxt(n)
        while fast != 1 and slow != fast:
            slow = nxt(slow); fast = nxt(nxt(fast))
        return fast == 1
