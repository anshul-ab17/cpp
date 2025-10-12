# LC 344. Reverse String | Easy
class Solution:
    def reverseString_brute(self, s):
        s[:] = s[::-1]

    # Two pointers - O(n) time, O(1) space
    def reverseString(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1; r -= 1
