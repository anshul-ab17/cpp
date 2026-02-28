class Solution:
    def toHex(self, num):
        if num == 0:
            return "0"

        if num < 0:
            num += 2 ** 32

        chars = "0123456789abcdef"
        ans = ""

        while num:
            ans = chars[num % 16] + ans
            num //= 16

        return ans
