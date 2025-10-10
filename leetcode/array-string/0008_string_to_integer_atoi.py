class Solution:
    def myAtoi(self, s):
        s = s.lstrip()

        if not s:
            return 0

        sign = -1 if s[0] == '-' else 1
        if s[0] in '+-':
            s = s[1:]

        num = 0

        for ch in s:
            if not ch.isdigit():
                break

            num = num * 10 + int(ch)

        num *= sign

        return max(-(2**31), min(2**31 - 1, num))
