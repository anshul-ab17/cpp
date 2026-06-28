class Solution:
    def minFlipsCoherent(self, s: str) -> int:
        flip0 = 0
        flip1 = 0

        for i, ch in enumerate(s):
            if ch != ('0' if i % 2 == 0 else '1'):
                flip0 += 1

            if ch != ('1' if i % 2 == 0 else '0'):
                flip1 += 1

        return min(flip0, flip1)
