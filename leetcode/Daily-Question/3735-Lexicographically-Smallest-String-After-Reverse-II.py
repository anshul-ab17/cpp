class Solution:
    def smallestStringAfterReverse(self, s: str, k: int) -> str:
        n = len(s)
        chars = list(s)

        i = 0
        while i <= n - k:
            window = chars[i:i + k]
            rev_window = window[::-1]

            if rev_window < window:
                chars[i:i + k] = rev_window
                i += k
            else:
                i += 1

        return "".join(chars)
